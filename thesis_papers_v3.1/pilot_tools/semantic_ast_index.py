"""Build and query a gold-blind, evidence-carrying Python AST index.

This module deliberately implements a *certified static subset*, not a Python
runtime call graph.  It reads complete ``.py`` blobs directly from frozen bare
Git object stores and accepts a relation only when a syntactic binding proof is
unique.  Dynamic receivers, rebinding, star imports, and ambiguous imports are
rejected explicitly; there is no name-cooccurrence fallback.

The build CLI is restricted to the frozen ARB semantic reserve and its source
readiness report.  It never opens benchmark gold, qrel, patch, or answer files.
The query CLI exposes the minimal primitives used by the development pilot:
DEFS_AT, RESOLVE_UNIQUE, CALLEES_OF, CALLERS_OF, IMPORTS_OF, IMPORTERS_OF,
REFS_TO, AS_TEST, and USES_FIXTURE.
"""

from __future__ import annotations

import argparse
import ast
import builtins
import hashlib
import io
import json
import os
import subprocess
import tempfile
import tokenize
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Callable, Iterable, Iterator, Mapping, Sequence
from urllib.parse import quote, unquote


INDEX_STATUS = "QUERY_ONLY_SEMANTIC_INDEX_BUILT"
READY_STATUS = "READY_FOR_SEMANTIC_INDEX_BUILD"
SCHEMA_VERSION = 1
EDGE_CALLS = "CALLS"
EDGE_IMPORTS = "IMPORTS"
EDGE_REFS = "REFS_TO"
EDGE_AS_TEST = "AS_TEST"
EDGE_AS_FIXTURE = "AS_FIXTURE"
EDGE_USES_FIXTURE = "USES_FIXTURE"
ENTITY_FIELDS = (
    "repo",
    "commit",
    "path",
    "qualname",
    "lineno",
    "end_lineno",
    "kind",
    "blob_oid",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _resolution_class(result: Mapping[str, object]) -> str:
    if result.get("status") == "RESOLVED_UNIQUE":
        return "CERTIFIED"
    reason = str(result.get("reason", ""))
    return "AMBIGUOUS" if "AMBIGUOUS" in reason else "DYNAMIC"


def _candidate_ids(result: Mapping[str, object]) -> list[str]:
    values: list[str] = []
    for field_name in ("candidates", "static_candidates", "candidate_entity_ids"):
        raw = result.get(field_name, [])
        if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
            values.extend(str(item) for item in raw)
    target = result.get("target_entity_id")
    if target:
        values.append(str(target))
    return sorted(set(values))


def _compact_witness(witness: Mapping[str, object]) -> dict[str, object]:
    return {
        key: witness.get(key)
        for key in (
            "path",
            "blob_oid",
            "lineno",
            "col_offset",
            "end_lineno",
            "end_col_offset",
            "expression",
        )
        if key in witness
    }


def make_entity_id(record: Mapping[str, object]) -> str:
    """Return a reversible ID containing all eight required identity fields."""

    parts = []
    for name in ENTITY_FIELDS:
        if name not in record:
            raise ValueError(f"entity identity is missing {name}")
        parts.append(f"{name}={quote(str(record[name]), safe='')}")
    return "pyent:v1|" + "|".join(parts)


def parse_entity_id(entity_id: str) -> dict[str, object]:
    """Parse and validate a canonical EntityID without consulting the index."""

    prefix = "pyent:v1|"
    if not entity_id.startswith(prefix):
        raise ValueError("unsupported EntityID prefix")
    raw_parts = entity_id[len(prefix) :].split("|")
    if len(raw_parts) != len(ENTITY_FIELDS):
        raise ValueError("EntityID has the wrong field count")
    parsed: dict[str, object] = {}
    for expected_name, raw_part in zip(ENTITY_FIELDS, raw_parts):
        name, separator, raw_value = raw_part.partition("=")
        if not separator or name != expected_name:
            raise ValueError(f"EntityID field order mismatch: expected {expected_name}")
        value: object = unquote(raw_value)
        if name in {"lineno", "end_lineno"}:
            try:
                value = int(str(value))
            except ValueError as error:
                raise ValueError(f"EntityID {name} is not an integer") from error
        parsed[name] = value
    if make_entity_id(parsed) != entity_id:
        raise ValueError("EntityID is not in canonical percent-encoded form")
    return parsed


def _scope_id(entity_id: str, kind: str, lineno: int, col_offset: int) -> str:
    payload = f"{entity_id}\0{kind}\0{lineno}\0{col_offset}".encode("utf-8")
    return "pyscope:v1:" + hashlib.sha256(payload).hexdigest()


def _git(repo_dir: Path, *arguments: str) -> bytes:
    completed = subprocess.run(
        ["git", "-c", f"safe.directory={repo_dir.resolve()}", "-C", str(repo_dir), *arguments],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(arguments)} failed in {repo_dir.name}: {message}")
    return completed.stdout


def _repo_store(asset_root: Path, repo: str) -> Path:
    return asset_root / repo.replace("/", "__")


def _python_tree_entries(repo_dir: Path, commit: str) -> list[dict[str, object]]:
    raw = _git(repo_dir, "ls-tree", "-r", "-l", "-z", "--full-tree", commit)
    entries: list[dict[str, object]] = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, separator, raw_path = record.partition(b"\t")
        if not separator:
            raise ValueError(f"malformed ls-tree record for {commit}")
        fields = metadata.split()
        if len(fields) != 4 or fields[1] != b"blob":
            continue
        path = raw_path.decode("utf-8", errors="surrogateescape").replace("\\", "/")
        if not path.endswith(".py"):
            continue
        entries.append(
            {
                "path": path,
                "oid": fields[2].decode("ascii"),
                "bytes": int(fields[3]),
            }
        )
    return sorted(entries, key=lambda item: str(item["path"]))


def _read_blobs(repo_dir: Path, oids: Iterable[str]) -> Iterator[tuple[str, bytes]]:
    process = subprocess.Popen(
        [
            "git",
            "-c",
            f"safe.directory={repo_dir.resolve()}",
            "-C",
            str(repo_dir),
            "cat-file",
            "--batch",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert process.stdin is not None and process.stdout is not None
    try:
        for oid in oids:
            process.stdin.write(oid.encode("ascii") + b"\n")
            process.stdin.flush()
            header = process.stdout.readline().rstrip(b"\n")
            fields = header.split()
            if len(fields) != 3 or fields[1] != b"blob":
                raise RuntimeError(f"unexpected cat-file header for {oid}: {header!r}")
            size = int(fields[2])
            data = process.stdout.read(size)
            terminator = process.stdout.read(1)
            if len(data) != size or terminator != b"\n":
                raise RuntimeError(f"truncated cat-file response for {oid}")
            yield oid, data
    finally:
        process.stdin.close()
        return_code = process.wait(timeout=60)
        assert process.stderr is not None
        message = process.stderr.read().decode("utf-8", errors="replace").strip()
        process.stdout.close()
        process.stderr.close()
        if return_code != 0:
            raise RuntimeError(f"git cat-file failed in {repo_dir.name}: {message}")


def _decode_python(data: bytes) -> tuple[str, str]:
    encoding, _ = tokenize.detect_encoding(io.BytesIO(data).readline)
    return data.decode(encoding), encoding


def _module_names(paths: Sequence[str]) -> dict[str, str | None]:
    """Infer only modules justified by contiguous ``__init__.py`` packages."""

    package_dirs = {
        str(PurePosixPath(path).parent)
        for path in paths
        if PurePosixPath(path).name == "__init__.py"
    }
    result: dict[str, str | None] = {}
    for raw_path in paths:
        path = PurePosixPath(raw_path)
        if path.name == "__init__.py":
            directory = path.parent
            pieces: list[str] = []
            cursor = directory
            while str(cursor) not in ("", ".") and str(cursor) in package_dirs:
                pieces.append(cursor.name)
                cursor = cursor.parent
            result[raw_path] = ".".join(reversed(pieces)) if pieces else None
            continue
        pieces = [path.stem]
        cursor = path.parent
        while str(cursor) not in ("", ".") and str(cursor) in package_dirs:
            pieces.append(cursor.name)
            cursor = cursor.parent
        if len(pieces) > 1 or str(path.parent) in ("", "."):
            result[raw_path] = ".".join(reversed(pieces))
        else:
            # A non-package path (typically tests/) is intentionally not made
            # importable merely by replacing slashes with dots.
            result[raw_path] = None
    return result


def _expression_shape(node: ast.AST) -> dict[str, object]:
    if isinstance(node, ast.Name):
        return {"shape": "name", "root": node.id, "attrs": [], "text": node.id}
    attrs: list[str] = []
    cursor = node
    while isinstance(cursor, ast.Attribute):
        attrs.append(cursor.attr)
        cursor = cursor.value
    if isinstance(cursor, ast.Name):
        ordered = list(reversed(attrs))
        text = ".".join([cursor.id, *ordered])
        return {"shape": "attribute", "root": cursor.id, "attrs": ordered, "text": text}
    return {
        "shape": "dynamic_attribute",
        "root": None,
        "attrs": list(reversed(attrs)),
        "text": "<dynamic>." + ".".join(reversed(attrs)),
    }


def _node_witness(node: ast.AST, *, path: str, blob_oid: str, expression: str) -> dict[str, object]:
    return {
        "path": path,
        "blob_oid": blob_oid,
        "lineno": int(getattr(node, "lineno", 0)),
        "col_offset": int(getattr(node, "col_offset", 0)),
        "end_lineno": int(getattr(node, "end_lineno", getattr(node, "lineno", 0))),
        "end_col_offset": int(getattr(node, "end_col_offset", getattr(node, "col_offset", 0))),
        "expression": expression,
    }


@dataclass
class BindingBucket:
    definitions: list[dict[str, object]] = field(default_factory=list)
    imports: list[dict[str, object]] = field(default_factory=list)
    blocker_counts: Counter[str] = field(default_factory=Counter)
    blocker_examples: dict[str, dict[str, object]] = field(default_factory=dict)

    def add_blocker(self, kind: str, *, lineno: int, col_offset: int) -> None:
        self.blocker_counts[kind] += 1
        self.blocker_examples.setdefault(
            kind,
            {"kind": kind, "lineno": lineno, "col_offset": col_offset},
        )

    def to_record(self) -> dict[str, object]:
        return {
            "definitions": sorted(self.definitions, key=lambda item: str(item["entity_id"])),
            "imports": sorted(
                self.imports,
                key=lambda item: (
                    int(item.get("lineno", 0)),
                    int(item.get("col_offset", 0)),
                    str(item.get("bound_name", "")),
                ),
            ),
            "blocker_counts": dict(sorted(self.blocker_counts.items())),
            "blocker_examples": [self.blocker_examples[key] for key in sorted(self.blocker_examples)],
        }


@dataclass
class ScopeState:
    scope_id: str
    kind: str
    repo: str
    commit: str
    owner_entity_id: str
    parent_scope_id: str | None
    module_scope_id: str
    path: str
    blob_oid: str
    lineno: int
    end_lineno: int
    qual_prefix: str
    module_name: str | None
    class_entity_id: str | None = None
    receiver_names: tuple[str, ...] = ()
    receiver_rejections: dict[str, str] = field(default_factory=dict)
    bindings: dict[str, BindingBucket] = field(default_factory=dict)
    global_names: set[str] = field(default_factory=set)
    nonlocal_names: set[str] = field(default_factory=set)
    poisoned_names: dict[str, set[str]] = field(default_factory=dict)
    scope_poison_reasons: set[str] = field(default_factory=set)

    def bucket(self, name: str) -> BindingBucket:
        return self.bindings.setdefault(name, BindingBucket())

    def poison_name(self, name: str, reason: str) -> None:
        self.poisoned_names.setdefault(name, set()).add(reason)

    def to_record(self) -> dict[str, object]:
        return {
            "schema_version": SCHEMA_VERSION,
            "scope_id": self.scope_id,
            "kind": self.kind,
            "repo": self.repo,
            "commit": self.commit,
            "owner_entity_id": self.owner_entity_id,
            "parent_scope_id": self.parent_scope_id,
            "module_scope_id": self.module_scope_id,
            "path": self.path,
            "blob_oid": self.blob_oid,
            "lineno": self.lineno,
            "end_lineno": self.end_lineno,
            "qual_prefix": self.qual_prefix,
            "module_name": self.module_name,
            "class_entity_id": self.class_entity_id,
            "receiver_names": list(self.receiver_names),
            "receiver_rejections": dict(sorted(self.receiver_rejections.items())),
            "global_names": sorted(self.global_names),
            "nonlocal_names": sorted(self.nonlocal_names),
            "poisoned_names": {
                name: sorted(reasons) for name, reasons in sorted(self.poisoned_names.items())
            },
            "scope_poison_reasons": sorted(self.scope_poison_reasons),
            "bindings": {name: self.bindings[name].to_record() for name in sorted(self.bindings)},
        }


class RejectionLedger:
    def __init__(self, examples_per_key: int = 25) -> None:
        self.examples_per_key = examples_per_key
        self.counts: Counter[tuple[str, str]] = Counter()
        self.examples: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)

    def add(
        self,
        operation: str,
        reason: str,
        example: Mapping[str, object],
        *,
        occurrence_count: int = 1,
    ) -> None:
        if occurrence_count < 1:
            raise ValueError("rejection occurrence_count must be positive")
        key = (operation, reason)
        self.counts[key] += occurrence_count
        if len(self.examples[key]) < self.examples_per_key:
            self.examples[key].append(dict(example))

    def count_record(self) -> dict[str, dict[str, int]]:
        output: dict[str, dict[str, int]] = defaultdict(dict)
        for (operation, reason), count in sorted(self.counts.items()):
            output[operation][reason] = count
        return dict(output)

    def example_rows(self) -> Iterator[dict[str, object]]:
        for (operation, reason), rows in sorted(self.examples.items()):
            total = self.counts[(operation, reason)]
            for index, row in enumerate(rows, start=1):
                yield {
                    "schema_version": SCHEMA_VERSION,
                    "operation": operation,
                    "reason": reason,
                    "example_index": index,
                    "total_rejections_for_key": total,
                    **row,
                }


class FactExtractor(ast.NodeVisitor):
    """Extract definitions, bindings, and unresolved expression sites."""

    def __init__(
        self,
        *,
        repo: str,
        commit: str,
        path: str,
        blob_oid: str,
        text: str,
        module_name: str | None,
        entities: list[dict[str, object]],
        scopes: dict[str, ScopeState],
        fact_handle: io.TextIOBase,
    ) -> None:
        self.repo = repo
        self.commit = commit
        self.path = path
        self.blob_oid = blob_oid
        self.text = text
        self.module_name = module_name
        self.entities = entities
        self.scopes = scopes
        self.fact_handle = fact_handle
        self.fact_aggregates: dict[str, dict[str, object]] = {}
        self.conditional_depth = 0
        tree = ast.parse(text, filename=path)
        last_line = max(1, len(text.splitlines()))
        module_record = self._entity_record(
            qualname="<module>",
            lineno=1,
            end_lineno=last_line,
            kind="module",
            parent_scope_id=None,
            module_name=module_name,
        )
        entities.append(module_record)
        module_scope_id = _scope_id(module_record["entity_id"], "module", 1, 0)
        module_scope = ScopeState(
            scope_id=module_scope_id,
            kind="module",
            repo=repo,
            commit=commit,
            owner_entity_id=str(module_record["entity_id"]),
            parent_scope_id=None,
            module_scope_id=module_scope_id,
            path=path,
            blob_oid=blob_oid,
            lineno=1,
            end_lineno=last_line,
            qual_prefix="",
            module_name=module_name,
        )
        scopes[module_scope_id] = module_scope
        module_record["scope_id"] = module_scope_id
        self.scope_stack: list[ScopeState] = [module_scope]
        self.visit(tree)
        for key in sorted(self.fact_aggregates):
            self.fact_handle.write(canonical_json(self.fact_aggregates[key]) + "\n")

    @property
    def scope(self) -> ScopeState:
        return self.scope_stack[-1]

    def _entity_record(
        self,
        *,
        qualname: str,
        lineno: int,
        end_lineno: int,
        kind: str,
        parent_scope_id: str | None,
        module_name: str | None,
    ) -> dict[str, object]:
        record: dict[str, object] = {
            "schema_version": SCHEMA_VERSION,
            "repo": self.repo,
            "commit": self.commit,
            "path": self.path,
            "qualname": qualname,
            "lineno": lineno,
            "end_lineno": end_lineno,
            "kind": kind,
            "blob_oid": self.blob_oid,
            "module_name": module_name,
            "parent_scope_id": parent_scope_id,
            "definition_certainty": (
                "conditional_control_flow" if self.conditional_depth else "unconditional_syntax"
            ),
        }
        record["entity_id"] = make_entity_id(record)
        return record

    def _child_qualname(self, name: str) -> str:
        scope = self.scope
        if scope.kind == "module":
            return name
        if scope.kind == "class":
            return f"{scope.qual_prefix}.{name}"
        return f"{scope.qual_prefix}.<locals>.{name}"

    def _add_definition(self, entity: dict[str, object], node: ast.AST) -> None:
        self.scope.bucket(str(entity["qualname"]).split(".")[-1]).definitions.append(
            {
                "entity_id": entity["entity_id"],
                "lineno": int(getattr(node, "lineno", 0)),
                "col_offset": int(getattr(node, "col_offset", 0)),
                "available_after_lineno": int(getattr(node, "end_lineno", getattr(node, "lineno", 0))),
                "available_after_col_offset": int(
                    getattr(node, "end_col_offset", getattr(node, "col_offset", 0))
                ),
            }
        )

    def _write_fact(self, payload: Mapping[str, object]) -> None:
        witness = dict(payload["witness"])
        identity = {
            "fact_type": payload["fact_type"],
            "operation": payload["operation"],
            "scope_id": payload["scope_id"],
            "owner_entity_id": payload["owner_entity_id"],
            "shape": payload["shape"],
        }
        key = canonical_json(identity)
        existing = self.fact_aggregates.get(key)
        if existing is None:
            stored = dict(payload)
            stored["occurrence_count"] = 1
            stored["occurrence_witnesses"] = [_compact_witness(witness)]
            self.fact_aggregates[key] = stored
            return
        existing["occurrence_count"] = int(existing["occurrence_count"]) + 1
        existing["occurrence_witnesses"].append(_compact_witness(witness))

    def _record_expression(self, node: ast.AST, operation: str) -> None:
        shape = _expression_shape(node)
        self._write_fact(
            {
                "fact_type": "expression",
                "operation": operation,
                "scope_id": self.scope.scope_id,
                "owner_entity_id": self.scope.owner_entity_id,
                "shape": shape,
                "witness": _node_witness(
                    node,
                    path=self.path,
                    blob_oid=self.blob_oid,
                    expression=str(shape["text"]),
                ),
            }
        )

    def _record_decorator(self, node: ast.AST) -> dict[str, object]:
        target = node.func if isinstance(node, ast.Call) else node
        shape = _expression_shape(target)
        name_override: str | None = None
        if isinstance(node, ast.Call):
            for keyword in node.keywords:
                if keyword.arg == "name" and isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str):
                    name_override = keyword.value.value
        return {
            "shape": shape,
            "is_call": isinstance(node, ast.Call),
            "name_override": name_override,
            "witness": _node_witness(
                target,
                path=self.path,
                blob_oid=self.blob_oid,
                expression=str(shape["text"]),
            ),
        }

    def _bind_target(self, node: ast.AST, kind: str) -> None:
        if isinstance(node, (ast.Tuple, ast.List)):
            for item in node.elts:
                self._bind_target(item, kind)
        elif isinstance(node, ast.Starred):
            self._bind_target(node.value, kind)
        elif isinstance(node, ast.Name):
            self.scope.bucket(node.id).add_blocker(
                kind,
                lineno=int(getattr(node, "lineno", 0)),
                col_offset=int(getattr(node, "col_offset", 0)),
            )
        elif (
            isinstance(node, ast.Attribute)
            and node.attr == "__test__"
            and isinstance(node.value, ast.Name)
        ):
            self.scope.poison_name(node.value.id, "PYTEST_ENTITY_TEST_FLAG_WRITE")
        elif isinstance(node, ast.Subscript):
            value = node.value
            if (
                isinstance(value, ast.Call)
                and isinstance(value.func, ast.Name)
                and value.func.id in {"globals", "locals"}
            ):
                self.scope.scope_poison_reasons.add("DYNAMIC_NAMESPACE_MAPPING_WRITE")

    def _visit_conditional_statements(self, statements: Sequence[ast.stmt]) -> None:
        self.conditional_depth += 1
        try:
            for statement in statements:
                self.visit(statement)
        finally:
            self.conditional_depth -= 1

    def _bind_arguments(self, arguments: ast.arguments) -> tuple[str, ...]:
        names: list[str] = []
        all_args = [*arguments.posonlyargs, *arguments.args, *arguments.kwonlyargs]
        if arguments.vararg is not None:
            all_args.append(arguments.vararg)
        if arguments.kwarg is not None:
            all_args.append(arguments.kwarg)
        for argument in all_args:
            names.append(argument.arg)
            self.scope.bucket(argument.arg).add_blocker(
                "parameter",
                lineno=int(getattr(argument, "lineno", 0)),
                col_offset=int(getattr(argument, "col_offset", 0)),
            )
        return tuple(names)

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef, kind: str) -> None:
        qualname = self._child_qualname(node.name)
        decorators = [self._record_decorator(item) for item in node.decorator_list]
        entity = self._entity_record(
            qualname=qualname,
            lineno=node.lineno,
            end_lineno=int(getattr(node, "end_lineno", node.lineno)),
            kind=kind,
            parent_scope_id=self.scope.scope_id,
            module_name=self.module_name,
        )
        entity["name"] = node.name
        entity["decorators"] = decorators
        entity["parameters"] = [
            {"name": arg.arg, "lineno": int(getattr(arg, "lineno", node.lineno))}
            for arg in [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]
        ]
        if node.args.vararg is not None:
            entity["parameters"].append({"name": node.args.vararg.arg, "lineno": node.args.vararg.lineno})
        if node.args.kwarg is not None:
            entity["parameters"].append({"name": node.args.kwarg.arg, "lineno": node.args.kwarg.lineno})
        self.entities.append(entity)

        # Decorators, defaults, and annotations execute in the enclosing scope.
        for decorator in node.decorator_list:
            self.visit(decorator)
        for default in [*node.args.defaults, *node.args.kw_defaults]:
            if default is not None:
                self.visit(default)
        for argument in [*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs]:
            if argument.annotation is not None:
                self.visit(argument.annotation)
        if node.args.vararg is not None and node.args.vararg.annotation is not None:
            self.visit(node.args.vararg.annotation)
        if node.args.kwarg is not None and node.args.kwarg.annotation is not None:
            self.visit(node.args.kwarg.annotation)
        if node.returns is not None:
            self.visit(node.returns)
        # The function name becomes available only after defaults,
        # annotations, and decorators have completed.
        self._add_definition(entity, node)

        scope_id = _scope_id(str(entity["entity_id"]), kind, node.lineno, node.col_offset)
        receiver_names: tuple[str, ...] = ()
        receiver_rejections: dict[str, str] = {}
        direct_class = self.scope.kind == "class"
        positional = [*node.args.posonlyargs, *node.args.args]
        staticmethod_named = any(
            str(item["shape"].get("text")) == "staticmethod" for item in decorators
        )
        classmethod_syntax = any(
            str(item["shape"].get("text")) == "classmethod" and not item.get("is_call")
            for item in decorators
        )
        staticmethod_syntax = any(
            str(item["shape"].get("text")) == "staticmethod" and not item.get("is_call")
            for item in decorators
        )
        classmethod_builtin = classmethod_syntax and "classmethod" not in self.scope.bindings
        staticmethod_builtin = staticmethod_syntax and "staticmethod" not in self.scope.bindings
        if direct_class and positional and not staticmethod_named:
            first = positional[0].arg
            if first == "self" or (first == "cls" and classmethod_builtin):
                receiver_names = (first,)
        elif direct_class and positional and staticmethod_named and positional[0].arg in {"self", "cls"}:
            receiver_rejections[positional[0].arg] = (
                "STATICMETHOD_RECEIVER_NOT_INSTANCE"
                if staticmethod_builtin
                else "DECORATED_METHOD_RECEIVER_UNCERTAIN"
            )
        function_scope = ScopeState(
            scope_id=scope_id,
            kind="function",
            repo=self.repo,
            commit=self.commit,
            owner_entity_id=str(entity["entity_id"]),
            parent_scope_id=self.scope.scope_id,
            module_scope_id=self.scope.module_scope_id,
            path=self.path,
            blob_oid=self.blob_oid,
            lineno=node.lineno,
            end_lineno=int(getattr(node, "end_lineno", node.lineno)),
            qual_prefix=qualname,
            module_name=self.module_name,
            class_entity_id=self.scope.owner_entity_id if direct_class else self.scope.class_entity_id,
            receiver_names=receiver_names,
            receiver_rejections=receiver_rejections,
        )
        self.scopes[scope_id] = function_scope
        entity["scope_id"] = scope_id
        self.scope_stack.append(function_scope)
        self._bind_arguments(node.args)
        for statement in node.body:
            self.visit(statement)
        self.scope_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:  # noqa: N802
        self._visit_function(node, "function")

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:  # noqa: N802
        self._visit_function(node, "async_function")

    def visit_ClassDef(self, node: ast.ClassDef) -> None:  # noqa: N802
        qualname = self._child_qualname(node.name)
        entity = self._entity_record(
            qualname=qualname,
            lineno=node.lineno,
            end_lineno=int(getattr(node, "end_lineno", node.lineno)),
            kind="class",
            parent_scope_id=self.scope.scope_id,
            module_name=self.module_name,
        )
        entity["name"] = node.name
        entity["decorators"] = [self._record_decorator(item) for item in node.decorator_list]
        self.entities.append(entity)
        for expression in [*node.decorator_list, *node.bases, *[keyword.value for keyword in node.keywords]]:
            self.visit(expression)
        # The class name is not bound while decorators/bases/keywords run.
        self._add_definition(entity, node)
        scope_id = _scope_id(str(entity["entity_id"]), "class", node.lineno, node.col_offset)
        class_scope = ScopeState(
            scope_id=scope_id,
            kind="class",
            repo=self.repo,
            commit=self.commit,
            owner_entity_id=str(entity["entity_id"]),
            parent_scope_id=self.scope.scope_id,
            module_scope_id=self.scope.module_scope_id,
            path=self.path,
            blob_oid=self.blob_oid,
            lineno=node.lineno,
            end_lineno=int(getattr(node, "end_lineno", node.lineno)),
            qual_prefix=qualname,
            module_name=self.module_name,
            class_entity_id=str(entity["entity_id"]),
        )
        self.scopes[scope_id] = class_scope
        entity["scope_id"] = scope_id
        self.scope_stack.append(class_scope)
        for statement in node.body:
            self.visit(statement)
        self.scope_stack.pop()

    def visit_Lambda(self, node: ast.Lambda) -> None:  # noqa: N802
        for default in [*node.args.defaults, *node.args.kw_defaults]:
            if default is not None:
                self.visit(default)
        scope_id = _scope_id(self.scope.owner_entity_id, "lambda", node.lineno, node.col_offset)
        lambda_scope = ScopeState(
            scope_id=scope_id,
            kind="lambda",
            repo=self.repo,
            commit=self.commit,
            owner_entity_id=self.scope.owner_entity_id,
            parent_scope_id=self.scope.scope_id,
            module_scope_id=self.scope.module_scope_id,
            path=self.path,
            blob_oid=self.blob_oid,
            lineno=node.lineno,
            end_lineno=int(getattr(node, "end_lineno", node.lineno)),
            qual_prefix=self.scope.qual_prefix,
            module_name=self.module_name,
            class_entity_id=self.scope.class_entity_id,
        )
        self.scopes[scope_id] = lambda_scope
        self.scope_stack.append(lambda_scope)
        self._bind_arguments(node.args)
        self.visit(node.body)
        self.scope_stack.pop()

    def _visit_comprehension(self, node: ast.AST, value_nodes: Sequence[ast.AST]) -> None:
        generators = list(getattr(node, "generators"))
        if not generators:
            for item in value_nodes:
                self.visit(item)
            return
        self.visit(generators[0].iter)
        scope_id = _scope_id(self.scope.owner_entity_id, "comprehension", node.lineno, node.col_offset)
        comp_scope = ScopeState(
            scope_id=scope_id,
            kind="comprehension",
            repo=self.repo,
            commit=self.commit,
            owner_entity_id=self.scope.owner_entity_id,
            parent_scope_id=self.scope.scope_id,
            module_scope_id=self.scope.module_scope_id,
            path=self.path,
            blob_oid=self.blob_oid,
            lineno=node.lineno,
            end_lineno=int(getattr(node, "end_lineno", node.lineno)),
            qual_prefix=self.scope.qual_prefix,
            module_name=self.module_name,
            class_entity_id=self.scope.class_entity_id,
        )
        self.scopes[scope_id] = comp_scope
        self.scope_stack.append(comp_scope)
        for index, generator in enumerate(generators):
            if index:
                self.visit(generator.iter)
            self._bind_target(generator.target, "comprehension_target")
            for condition in generator.ifs:
                self.visit(condition)
        for item in value_nodes:
            self.visit(item)
        self.scope_stack.pop()

    def visit_ListComp(self, node: ast.ListComp) -> None:  # noqa: N802
        self._visit_comprehension(node, [node.elt])

    def visit_SetComp(self, node: ast.SetComp) -> None:  # noqa: N802
        self._visit_comprehension(node, [node.elt])

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:  # noqa: N802
        self._visit_comprehension(node, [node.elt])

    def visit_DictComp(self, node: ast.DictComp) -> None:  # noqa: N802
        self._visit_comprehension(node, [node.key, node.value])

    def visit_Import(self, node: ast.Import) -> None:  # noqa: N802
        for alias in node.names:
            bound_name = alias.asname or alias.name.split(".")[0]
            self.scope.bucket(bound_name).imports.append(
                {
                    "style": "import",
                    "bound_name": bound_name,
                    "imported_module": alias.name,
                    "asname": alias.asname,
                    "lineno": node.lineno,
                    "col_offset": node.col_offset,
                    "end_lineno": int(getattr(node, "end_lineno", node.lineno)),
                    "path": self.path,
                    "blob_oid": self.blob_oid,
                    "owner_entity_id": self.scope.owner_entity_id,
                    "definition_certainty": (
                        "conditional_control_flow" if self.conditional_depth else "unconditional_syntax"
                    ),
                }
            )

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # noqa: N802
        for alias in node.names:
            if alias.name == "*":
                bound_name = "*"
                self.scope.scope_poison_reasons.add("STAR_IMPORT_DYNAMIC_NAMESPACE")
            else:
                bound_name = alias.asname or alias.name
            self.scope.bucket(bound_name).imports.append(
                {
                    "style": "from",
                    "bound_name": bound_name,
                    "module": node.module,
                    "level": node.level,
                    "imported_name": alias.name,
                    "asname": alias.asname,
                    "lineno": node.lineno,
                    "col_offset": node.col_offset,
                    "end_lineno": int(getattr(node, "end_lineno", node.lineno)),
                    "path": self.path,
                    "blob_oid": self.blob_oid,
                    "owner_entity_id": self.scope.owner_entity_id,
                    "definition_certainty": (
                        "conditional_control_flow" if self.conditional_depth else "unconditional_syntax"
                    ),
                }
            )

    def visit_Global(self, node: ast.Global) -> None:  # noqa: N802
        self.scope.global_names.update(node.names)
        module_scope = self.scopes[self.scope.module_scope_id]
        for name in node.names:
            self.scope.poison_name(name, "GLOBAL_DECLARATION_STORE_UNMODELED")
            module_scope.poison_name(name, "GLOBAL_DECLARATION_STORE_UNMODELED")

    def visit_Nonlocal(self, node: ast.Nonlocal) -> None:  # noqa: N802
        self.scope.nonlocal_names.update(node.names)
        enclosing = next(
            (
                scope
                for scope in reversed(self.scope_stack[:-1])
                if scope.kind in {"function", "lambda", "comprehension"}
            ),
            None,
        )
        for name in node.names:
            self.scope.poison_name(name, "NONLOCAL_DECLARATION_STORE_UNMODELED")
            if enclosing is not None:
                enclosing.poison_name(name, "NONLOCAL_DECLARATION_STORE_UNMODELED")

    def visit_Assign(self, node: ast.Assign) -> None:  # noqa: N802
        self.visit(node.value)
        for target in node.targets:
            self._bind_target(target, "assignment")
            if not isinstance(target, ast.Name):
                self.visit(target)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:  # noqa: N802
        if node.value is not None:
            self.visit(node.value)
        self.visit(node.annotation)
        self._bind_target(node.target, "assignment")
        if not isinstance(node.target, ast.Name):
            self.visit(node.target)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:  # noqa: N802
        self.visit(node.value)
        self._bind_target(node.target, "augmented_assignment")
        if not isinstance(node.target, ast.Name):
            self.visit(node.target)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:  # noqa: N802
        self.visit(node.value)
        if self.scope.kind == "comprehension" and isinstance(node.target, ast.Name):
            self.scope.poison_name(node.target.id, "COMPREHENSION_WALRUS_SCOPE_UNMODELED")
            outer = next(
                (scope for scope in reversed(self.scope_stack[:-1]) if scope.kind != "comprehension"),
                None,
            )
            if outer is not None:
                outer.poison_name(node.target.id, "COMPREHENSION_WALRUS_SCOPE_UNMODELED")
        self._bind_target(node.target, "named_expression")

    def visit_TypeAlias(self, node: ast.AST) -> None:  # noqa: N802
        # Python 3.12 ``type A = ...`` is a real binding and must block a
        # same-named function/class from being treated as uniquely callable.
        name = getattr(node, "name", None)
        if isinstance(name, ast.Name):
            self._bind_target(name, "type_alias")
        for type_parameter in getattr(node, "type_params", []):
            self.visit(type_parameter)
        value = getattr(node, "value", None)
        if isinstance(value, ast.AST):
            self.visit(value)

    def visit_For(self, node: ast.For) -> None:  # noqa: N802
        self.visit(node.iter)
        self._bind_target(node.target, "loop_target")
        self._visit_conditional_statements(node.body)
        self._visit_conditional_statements(node.orelse)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:  # noqa: N802
        self.visit_For(node)

    def visit_If(self, node: ast.If) -> None:  # noqa: N802
        self.visit(node.test)
        self._visit_conditional_statements(node.body)
        self._visit_conditional_statements(node.orelse)

    def visit_While(self, node: ast.While) -> None:  # noqa: N802
        self.visit(node.test)
        self._visit_conditional_statements(node.body)
        self._visit_conditional_statements(node.orelse)

    def _visit_try(self, node: ast.Try | ast.TryStar) -> None:
        self._visit_conditional_statements(node.body)
        for handler in node.handlers:
            self.conditional_depth += 1
            try:
                self.visit(handler)
            finally:
                self.conditional_depth -= 1
        self._visit_conditional_statements(node.orelse)
        self._visit_conditional_statements(node.finalbody)

    def visit_Try(self, node: ast.Try) -> None:  # noqa: N802
        self._visit_try(node)

    def visit_TryStar(self, node: ast.TryStar) -> None:  # noqa: N802
        self._visit_try(node)

    def visit_With(self, node: ast.With) -> None:  # noqa: N802
        for item in node.items:
            self.visit(item.context_expr)
            if item.optional_vars is not None:
                self._bind_target(item.optional_vars, "with_target")
        self._visit_conditional_statements(node.body)

    def visit_AsyncWith(self, node: ast.AsyncWith) -> None:  # noqa: N802
        self.visit_With(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:  # noqa: N802
        if node.type is not None:
            self.visit(node.type)
        if node.name:
            self.scope.bucket(node.name).add_blocker(
                "exception_target", lineno=node.lineno, col_offset=node.col_offset
            )
        for statement in node.body:
            self.visit(statement)

    def _bind_pattern(self, pattern: ast.pattern) -> None:
        if isinstance(pattern, ast.MatchAs):
            if pattern.pattern is not None:
                self._bind_pattern(pattern.pattern)
            if pattern.name:
                self.scope.bucket(pattern.name).add_blocker(
                    "match_pattern", lineno=pattern.lineno, col_offset=pattern.col_offset
                )
        elif isinstance(pattern, ast.MatchStar):
            if pattern.name:
                self.scope.bucket(pattern.name).add_blocker(
                    "match_pattern", lineno=pattern.lineno, col_offset=pattern.col_offset
                )
        elif isinstance(pattern, ast.MatchMapping):
            for nested in pattern.patterns:
                self._bind_pattern(nested)
            if pattern.rest:
                self.scope.bucket(pattern.rest).add_blocker(
                    "match_pattern", lineno=pattern.lineno, col_offset=pattern.col_offset
                )
        elif isinstance(pattern, ast.MatchClass):
            self.visit(pattern.cls)
            for nested in [*pattern.patterns, *pattern.kwd_patterns]:
                self._bind_pattern(nested)
        elif isinstance(pattern, ast.MatchSequence):
            for nested in pattern.patterns:
                self._bind_pattern(nested)
        elif isinstance(pattern, ast.MatchOr):
            for nested in pattern.patterns:
                self._bind_pattern(nested)
        elif isinstance(pattern, ast.MatchValue):
            self.visit(pattern.value)

    def visit_Match(self, node: ast.Match) -> None:  # noqa: N802
        self.visit(node.subject)
        for case in node.cases:
            self._bind_pattern(case.pattern)
            if case.guard is not None:
                self.visit(case.guard)
            self._visit_conditional_statements(case.body)

    def visit_Delete(self, node: ast.Delete) -> None:  # noqa: N802
        for target in node.targets:
            self._bind_target(target, "delete_target")
            if not isinstance(target, ast.Name):
                self.visit(target)

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802
        if isinstance(node.func, ast.Name) and node.func.id == "exec":
            self.scope.scope_poison_reasons.add("EXEC_DYNAMIC_NAMESPACE")
        self._record_expression(node.func, "CALLEES_OF")
        self.visit(node.func)
        for argument in node.args:
            self.visit(argument)
        for keyword in node.keywords:
            self.visit(keyword.value)

    def visit_Attribute(self, node: ast.Attribute) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            self._record_expression(node, "REFS_TO")
            shape = _expression_shape(node)
            if shape["shape"] == "dynamic_attribute":
                self.visit(node.value)
        else:
            self.visit(node.value)

    def visit_Name(self, node: ast.Name) -> None:  # noqa: N802
        if isinstance(node.ctx, ast.Load):
            self._record_expression(node, "REFS_TO")


def _public_entity(record: Mapping[str, object]) -> dict[str, object]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def _relative_module(current_module: str | None, path: str, module: str | None, level: int) -> str | None:
    if level == 0:
        return module
    if current_module is None:
        return None
    current_parts = current_module.split(".")
    is_package_init = PurePosixPath(path).name == "__init__.py"
    package_parts = current_parts if is_package_init else current_parts[:-1]
    ascend = level - 1
    if ascend > len(package_parts):
        return None
    base = package_parts[: len(package_parts) - ascend]
    if module:
        base.extend(module.split("."))
    return ".".join(base) if base else None


class Resolver:
    """Unique-binding resolver shared by builds and persisted primitive queries."""

    def __init__(self, entities: Mapping[str, Mapping[str, object]], scopes: Mapping[str, Mapping[str, object]]) -> None:
        self.entities = entities
        self.scopes = scopes
        self.module_entities: dict[tuple[str, str, str], list[str]] = defaultdict(list)
        self.module_qual_entities: dict[tuple[str, str, str, str], list[str]] = defaultdict(list)
        self.entity_scopes: dict[str, str] = {}
        for entity_id, entity in entities.items():
            repo = str(entity["repo"])
            commit = str(entity["commit"])
            module_name = entity.get("module_name")
            if module_name:
                if entity.get("kind") == "module":
                    self.module_entities[(repo, commit, str(module_name))].append(entity_id)
                else:
                    self.module_qual_entities[
                        (repo, commit, str(module_name), str(entity["qualname"]))
                    ].append(entity_id)
            scope_id = entity.get("scope_id")
            if scope_id:
                self.entity_scopes[entity_id] = str(scope_id)
        for scope_id, scope in scopes.items():
            owner_id = str(scope["owner_entity_id"])
            if owner_id not in entities:
                raise ValueError(f"scope owner is missing from entity index: {scope_id}")
            owner = entities[owner_id]
            partition = (str(scope["repo"]), str(scope["commit"]))
            owner_partition = (str(owner["repo"]), str(owner["commit"]))
            if partition != owner_partition:
                raise ValueError(f"scope/entity snapshot partition mismatch: {scope_id}")
            parent_id = scope.get("parent_scope_id")
            if parent_id:
                parent = scopes[str(parent_id)]
                parent_partition = (str(parent["repo"]), str(parent["commit"]))
                if partition != parent_partition:
                    raise ValueError(f"scope parent crosses snapshot partition: {scope_id}")
        for values in self.module_entities.values():
            values.sort()
        for values in self.module_qual_entities.values():
            values.sort()

    @staticmethod
    def _rejected(reason: str, **extra: object) -> dict[str, object]:
        return {"status": "REJECTED", "reason": reason, **extra}

    @staticmethod
    def _resolved(entity_id: str, strategy: str, **extra: object) -> dict[str, object]:
        return {
            "status": "RESOLVED_UNIQUE",
            "target_entity_id": entity_id,
            "proof": {"strategy": strategy, **extra},
        }

    def _parent_for_lookup(self, scope: Mapping[str, object]) -> str | None:
        parent_id = scope.get("parent_scope_id")
        if not parent_id:
            return None
        parent = self.scopes[str(parent_id)]
        if scope.get("kind") in {"function", "lambda", "comprehension"} and parent.get("kind") == "class":
            parent_id = parent.get("parent_scope_id")
        return str(parent_id) if parent_id else None

    def _scope_partition(self, scope_id: str) -> tuple[str, str]:
        scope = self.scopes[scope_id]
        return str(scope["repo"]), str(scope["commit"])

    def _cross_partition_candidates(self, scope_id: str, candidates: Sequence[str]) -> list[str]:
        partition = self._scope_partition(scope_id)
        return sorted(
            entity_id
            for entity_id in candidates
            if (
                str(self.entities[entity_id]["repo"]),
                str(self.entities[entity_id]["commit"]),
            )
            != partition
        )

    def _entity_binding_rejection(self, entity_id: str) -> str | None:
        entity = self.entities[entity_id]
        if entity.get("definition_certainty") != "unconditional_syntax":
            return "CONDITIONAL_BINDING_NOT_DOMINATING"
        decorators = list(entity.get("decorators", []))
        if decorators:
            return "DECORATED_BINDING_MAY_REPLACE"
        parent_scope_id = entity.get("parent_scope_id")
        parent = self.scopes.get(str(parent_scope_id)) if parent_scope_id else None
        if parent is None or parent.get("kind") != "module":
            return None
        scope_poison = list(parent.get("scope_poison_reasons", []))
        if scope_poison:
            return "TARGET_MODULE_BINDINGS_POISONED"
        name = str(entity.get("name") or entity.get("qualname", "").split(".")[-1])
        if name in dict(parent.get("poisoned_names", {})):
            return "TARGET_EXPORT_BINDING_POISONED"
        bucket = dict(parent.get("bindings", {})).get(name)
        if not isinstance(bucket, Mapping):
            return "TARGET_EXPORT_BINDING_MISSING"
        definitions = [str(item["entity_id"]) for item in bucket.get("definitions", [])]
        blocker_counts = dict(bucket.get("blocker_counts", {}))
        blocker_total = sum(int(value) for value in blocker_counts.values())
        if int(blocker_counts.get("type_alias", 0)):
            return "DYNAMIC_OR_REBOUND_LOCAL"
        if definitions != [entity_id] or bucket.get("imports") or blocker_total:
            return "TARGET_EXPORT_DYNAMIC_OR_REBOUND"
        return None

    def _bucket_lookup(self, start_scope_id: str, name: str) -> tuple[Mapping[str, object] | None, str | None]:
        scope_id: str | None = start_scope_id
        visited: set[str] = set()
        while scope_id is not None and scope_id not in visited:
            visited.add(scope_id)
            scope = self.scopes[scope_id]
            if name in set(scope.get("global_names", [])):
                scope_id = str(scope["module_scope_id"])
                scope = self.scopes[scope_id]
            elif name in set(scope.get("nonlocal_names", [])):
                parent_id = self._parent_for_lookup(scope)
                while parent_id and self.scopes[parent_id].get("kind") not in {"function", "lambda", "comprehension"}:
                    parent_id = self._parent_for_lookup(self.scopes[parent_id])
                scope_id = parent_id
                continue
            bindings = scope.get("bindings", {})
            if isinstance(bindings, Mapping) and name in bindings:
                return bindings[name], scope_id
            scope_id = self._parent_for_lookup(scope)
        return None, None

    def _poison_lookup(self, start_scope_id: str, name: str) -> dict[str, object] | None:
        scope_id: str | None = start_scope_id
        visited: set[str] = set()
        while scope_id is not None and scope_id not in visited:
            visited.add(scope_id)
            scope = self.scopes[scope_id]
            scope_reasons = sorted(str(item) for item in scope.get("scope_poison_reasons", []))
            if scope_reasons:
                return self._rejected(
                    "SCOPE_BINDINGS_POISONED",
                    expression=name,
                    poison_reasons=scope_reasons,
                    poisoned_scope_id=scope_id,
                )
            poisoned_names = dict(scope.get("poisoned_names", {}))
            if name in poisoned_names:
                reasons = sorted(str(item) for item in poisoned_names[name])
                return self._rejected(
                    reasons[0] if len(reasons) == 1 else "NAME_BINDING_POISONED",
                    expression=name,
                    poison_reasons=reasons,
                    poisoned_scope_id=scope_id,
                )
            scope_id = self._parent_for_lookup(scope)
        return None

    def _binding_candidates(self, bucket: Mapping[str, object]) -> tuple[list[str], list[Mapping[str, object]], int]:
        candidates = [str(item["entity_id"]) for item in bucket.get("definitions", [])]
        imports: list[Mapping[str, object]] = list(bucket.get("imports", []))
        for item in imports:
            if item.get("resolution_status") == "RESOLVED_UNIQUE" and item.get("target_entity_id"):
                candidates.append(str(item["target_entity_id"]))
            for candidate in item.get("candidate_entity_ids", []):
                candidates.append(str(candidate))
        blocker_total = sum(int(value) for value in dict(bucket.get("blocker_counts", {})).values())
        return sorted(set(candidates)), imports, blocker_total

    @staticmethod
    def _candidate_binding_positions(bucket: Mapping[str, object]) -> list[tuple[str, int, int]]:
        positioned: list[tuple[str, int, int]] = []
        for item in bucket.get("definitions", []):
            positioned.append(
                (
                    str(item["entity_id"]),
                    int(item.get("available_after_lineno", item.get("lineno", 0))),
                    int(item.get("available_after_col_offset", item.get("col_offset", 0))),
                )
            )
        for item in bucket.get("imports", []):
            targets: list[str] = []
            if item.get("target_entity_id"):
                targets.append(str(item["target_entity_id"]))
            targets.extend(str(value) for value in item.get("candidate_entity_ids", []))
            for target in sorted(set(targets)):
                positioned.append(
                    (target, int(item.get("lineno", 0)), int(item.get("col_offset", 0)))
                )
        return positioned

    def _apply_same_scope_dominance(
        self,
        *,
        start_scope_id: str,
        binding_scope_id: str | None,
        bucket: Mapping[str, object],
        candidates: Sequence[str],
        lineno: int,
        col_offset: int,
        expression: object,
    ) -> tuple[list[str], dict[str, object] | None]:
        if binding_scope_id != start_scope_id:
            # A function body can execute before a later module binding has
            # been initialized (for example, an eager call between the two
            # definitions).  The conservative certificate therefore only
            # admits enclosing-module bindings that were already available
            # when the source function definition began.  This deliberately
            # rejects some safe forward references instead of assuming an
            # unobserved module-initialization order.
            start_scope = self.scopes[start_scope_id]
            binding_scope = self.scopes.get(str(binding_scope_id)) if binding_scope_id else None
            if start_scope.get("kind") == "function" and binding_scope and binding_scope.get("kind") == "module":
                owner = self.entities[str(start_scope["owner_entity_id"])]
                source_definition_position = (
                    int(owner.get("lineno", 0)),
                    0,
                )
                dominant: set[str] = set()
                non_dominating: set[str] = set()
                for entity_id, binding_line, binding_col in self._candidate_binding_positions(bucket):
                    if (binding_line, binding_col) < source_definition_position:
                        dominant.add(entity_id)
                    else:
                        non_dominating.add(entity_id)
                non_dominating.difference_update(dominant)
                if non_dominating:
                    return sorted(dominant), self._rejected(
                        "CROSS_SCOPE_BINDING_NOT_AVAILABLE_AT_FUNCTION_DEFINITION",
                        expression=expression,
                        static_candidates=sorted(set(candidates)),
                        non_dominating_candidates=sorted(non_dominating),
                        source_definition_position={
                            "lineno": source_definition_position[0],
                            "col_offset": source_definition_position[1],
                        },
                    )
                return sorted(dominant or set(candidates)), None
            return list(candidates), None
        dominant: set[str] = set()
        non_dominating: set[str] = set()
        site_position = (lineno, col_offset)
        for entity_id, binding_line, binding_col in self._candidate_binding_positions(bucket):
            if (binding_line, binding_col) < site_position:
                dominant.add(entity_id)
            else:
                non_dominating.add(entity_id)
        # A target with at least one dominating binding remains dominating;
        # later duplicate/rebinding is still rejected as a competitor.
        non_dominating.difference_update(dominant)
        if non_dominating:
            reason = (
                "BINDING_NOT_DOMINATING_SITE"
                if not dominant
                else "NON_DOMINATING_COMPETING_BINDING"
            )
            return sorted(dominant), self._rejected(
                reason,
                expression=expression,
                static_candidates=sorted(set(candidates)),
                non_dominating_candidates=sorted(non_dominating),
                site_position={"lineno": lineno, "col_offset": col_offset},
            )
        return sorted(dominant or set(candidates)), None

    def resolve_name(
        self,
        scope_id: str,
        name: str,
        *,
        lineno: int,
        col_offset: int,
    ) -> dict[str, object]:
        poison = self._poison_lookup(scope_id, name)
        if poison is not None:
            return poison
        bucket, binding_scope_id = self._bucket_lookup(scope_id, name)
        if bucket is None:
            reason = "BUILTIN_NAME" if name in dir(builtins) else "UNRESOLVED_NAME"
            return self._rejected(reason, expression=name)
        candidates, imports, blocker_total = self._binding_candidates(bucket)
        candidates, dominance_rejection = self._apply_same_scope_dominance(
            start_scope_id=scope_id,
            binding_scope_id=binding_scope_id,
            bucket=bucket,
            candidates=candidates,
            lineno=lineno,
            col_offset=col_offset,
            expression=name,
        )
        if dominance_rejection is not None:
            return dominance_rejection
        cross_partition = self._cross_partition_candidates(scope_id, candidates)
        if cross_partition:
            return self._rejected(
                "CROSS_SNAPSHOT_BINDING_CORRUPTION",
                expression=name,
                candidates=candidates,
                cross_snapshot_candidates=cross_partition,
            )
        import_binding_rejections = sorted(
            {
                str(item["rejection_reason"])
                for item in imports
                if item.get("resolution_status") == "REJECTED" and item.get("rejection_reason")
            }
        )
        if import_binding_rejections and candidates:
            return self._rejected(
                (
                    import_binding_rejections[0]
                    if len(import_binding_rejections) == 1
                    else "AMBIGUOUS_OR_UNSTABLE_IMPORT_BINDING"
                ),
                expression=name,
                static_candidates=candidates,
                import_reasons=import_binding_rejections,
            )
        unstable = {
            entity_id: reason
            for entity_id in candidates
            if (reason := self._entity_binding_rejection(entity_id)) is not None
        }
        if unstable:
            reasons = sorted(set(unstable.values()))
            return self._rejected(
                reasons[0] if len(reasons) == 1 else "MULTIPLE_UNSTABLE_BINDINGS",
                expression=name,
                static_candidates=candidates,
                candidate_rejections=unstable,
            )
        if binding_scope_id and self.scopes[binding_scope_id].get("kind") == "class":
            return self._rejected(
                "CLASS_BODY_EXECUTION_ORDER_UNCERTAIN",
                expression=name,
                binding_scope_id=binding_scope_id,
                static_candidates=candidates,
            )
        if blocker_total:
            return self._rejected(
                "DYNAMIC_OR_REBOUND_LOCAL",
                expression=name,
                binding_scope_id=binding_scope_id,
                static_candidates=candidates,
                blocker_counts=bucket.get("blocker_counts", {}),
            )
        if len(candidates) == 1:
            return self._resolved(candidates[0], "lexical_unique_binding", binding_scope_id=binding_scope_id)
        if len(candidates) > 1:
            return self._rejected(
                "AMBIGUOUS_BINDING",
                expression=name,
                binding_scope_id=binding_scope_id,
                candidates=candidates,
            )
        import_reasons = sorted({str(item.get("rejection_reason")) for item in imports if item.get("rejection_reason")})
        if import_reasons:
            return self._rejected(
                import_reasons[0] if len(import_reasons) == 1 else "AMBIGUOUS_OR_UNRESOLVED_IMPORT",
                expression=name,
                binding_scope_id=binding_scope_id,
                import_reasons=import_reasons,
            )
        return self._rejected("UNRESOLVED_BINDING", expression=name, binding_scope_id=binding_scope_id)

    def _resolve_module_qualname(self, dotted: str, *, repo: str, commit: str) -> dict[str, object]:
        pieces = dotted.split(".")
        candidates: list[tuple[int, str]] = []
        for index in range(len(pieces), 0, -1):
            module_name = ".".join(pieces[:index])
            modules = self.module_entities.get((repo, commit, module_name), [])
            if len(modules) != 1:
                continue
            remainder = ".".join(pieces[index:])
            if not remainder:
                candidates.append((index, modules[0]))
            else:
                for entity_id in self.module_qual_entities.get((repo, commit, module_name, remainder), []):
                    candidates.append((index, entity_id))
            if candidates:
                break
        entity_ids = sorted({entity_id for _, entity_id in candidates})
        if len(entity_ids) == 1:
            binding_rejection = self._entity_binding_rejection(entity_ids[0])
            if binding_rejection:
                return self._rejected(
                    binding_rejection,
                    expression=dotted,
                    static_candidates=entity_ids,
                )
            return self._resolved(
                entity_ids[0],
                "imported_module_qualified_lookup",
                dotted=dotted,
                snapshot_partition={"repo": repo, "commit": commit},
            )
        if len(entity_ids) > 1:
            return self._rejected("AMBIGUOUS_MODULE_QUALNAME", expression=dotted, candidates=entity_ids)
        return self._rejected("UNRESOLVED_MODULE_QUALNAME", expression=dotted)

    def _class_member(self, class_entity_id: str, attrs: Sequence[str], strategy: str) -> dict[str, object]:
        class_entity = self.entities.get(class_entity_id)
        if not class_entity or class_entity.get("kind") != "class":
            return self._rejected("DYNAMIC_ATTRIBUTE_RECEIVER", receiver_entity_id=class_entity_id)
        module_name = class_entity.get("module_name")
        if not module_name:
            return self._rejected("NONIMPORTABLE_CLASS_MODULE", receiver_entity_id=class_entity_id)
        qualname = ".".join([str(class_entity["qualname"]), *attrs])
        repo = str(class_entity["repo"])
        commit = str(class_entity["commit"])
        candidates = self.module_qual_entities.get((repo, commit, str(module_name), qualname), [])
        if len(candidates) == 1:
            binding_rejection = self._entity_binding_rejection(candidates[0])
            if binding_rejection:
                return self._rejected(
                    binding_rejection,
                    expression=qualname,
                    static_candidates=candidates,
                )
            return self._resolved(candidates[0], strategy, receiver_entity_id=class_entity_id)
        if len(candidates) > 1:
            return self._rejected("AMBIGUOUS_CLASS_MEMBER", candidates=candidates, qualname=qualname)
        return self._rejected("UNRESOLVED_CLASS_MEMBER", qualname=qualname)

    def _resolve_expression_candidate(
        self,
        scope_id: str,
        shape: Mapping[str, object],
        *,
        lineno: int | None,
        col_offset: int | None,
    ) -> dict[str, object]:
        if lineno is None or col_offset is None:
            return self._rejected("SITE_POSITION_REQUIRED", expression=shape.get("text"))
        if shape.get("shape") == "dynamic_attribute":
            return self._rejected("DYNAMIC_ATTRIBUTE_RECEIVER", expression=shape.get("text"))
        root = str(shape.get("root"))
        attrs = [str(item) for item in shape.get("attrs", [])]
        poison = self._poison_lookup(scope_id, root)
        if poison is not None:
            return poison
        if not attrs:
            return self.resolve_name(
                scope_id,
                root,
                lineno=lineno,
                col_offset=col_offset,
            )
        scope = self.scopes[scope_id]
        repo, commit = self._scope_partition(scope_id)
        receiver_rejections = dict(scope.get("receiver_rejections", {}))
        if root in receiver_rejections:
            return self._rejected(str(receiver_rejections[root]), expression=shape.get("text"))
        if root in set(scope.get("receiver_names", [])) and scope.get("class_entity_id"):
            return self._class_member(str(scope["class_entity_id"]), attrs, "same_class_receiver")

        bucket, binding_scope_id = self._bucket_lookup(scope_id, root)
        if bucket is None:
            return self._rejected("UNRESOLVED_ATTRIBUTE_ROOT", expression=shape.get("text"))
        candidates, imports, blocker_total = self._binding_candidates(bucket)
        candidates, dominance_rejection = self._apply_same_scope_dominance(
            start_scope_id=scope_id,
            binding_scope_id=binding_scope_id,
            bucket=bucket,
            candidates=candidates,
            lineno=lineno,
            col_offset=col_offset,
            expression=shape.get("text"),
        )
        if dominance_rejection is not None:
            return dominance_rejection
        cross_partition = self._cross_partition_candidates(scope_id, candidates)
        if cross_partition:
            return self._rejected(
                "CROSS_SNAPSHOT_BINDING_CORRUPTION",
                expression=shape.get("text"),
                candidates=candidates,
                cross_snapshot_candidates=cross_partition,
            )
        import_binding_rejections = sorted(
            {
                str(item["rejection_reason"])
                for item in imports
                if item.get("resolution_status") == "REJECTED" and item.get("rejection_reason")
            }
        )
        if import_binding_rejections and candidates:
            return self._rejected(
                (
                    import_binding_rejections[0]
                    if len(import_binding_rejections) == 1
                    else "AMBIGUOUS_OR_UNSTABLE_IMPORT_BINDING"
                ),
                expression=shape.get("text"),
                static_candidates=candidates,
                import_reasons=import_binding_rejections,
            )
        unstable_roots = {
            entity_id: reason
            for entity_id in candidates
            if (reason := self._entity_binding_rejection(entity_id)) is not None
        }
        if unstable_roots:
            reasons = sorted(set(unstable_roots.values()))
            return self._rejected(
                reasons[0] if len(reasons) == 1 else "MULTIPLE_UNSTABLE_BINDINGS",
                expression=shape.get("text"),
                static_candidates=candidates,
                candidate_rejections=unstable_roots,
            )
        if binding_scope_id and self.scopes[binding_scope_id].get("kind") == "class":
            return self._rejected(
                "CLASS_BODY_EXECUTION_ORDER_UNCERTAIN",
                expression=shape.get("text"),
                binding_scope_id=binding_scope_id,
                static_candidates=candidates,
            )
        if blocker_total:
            return self._rejected(
                "DYNAMIC_OR_REBOUND_ATTRIBUTE_ROOT",
                expression=shape.get("text"),
                binding_scope_id=binding_scope_id,
                blocker_counts=bucket.get("blocker_counts", {}),
            )

        import_paths: list[str] = []
        for item in imports:
            if item.get("style") == "import":
                imported_module = str(item.get("imported_module"))
                asname = item.get("asname")
                if asname:
                    import_paths.append(".".join([imported_module, *attrs]))
                else:
                    full = ".".join([root, *attrs])
                    # ``import a.b`` certifies a.b and descendants, not any
                    # arbitrary attribute of a loaded as a side effect.
                    if full == imported_module or full.startswith(imported_module + "."):
                        import_paths.append(full)
            elif item.get("style") == "from" and item.get("canonical_symbol"):
                target = item.get("target_entity_id")
                if target and self.entities.get(str(target), {}).get("kind") == "class":
                    class_result = self._class_member(str(target), attrs, "imported_class_member")
                    if class_result["status"] == "RESOLVED_UNIQUE":
                        return class_result
                canonical = str(item["canonical_symbol"])
                import_paths.append(".".join([canonical, *attrs]))
        resolved_imports = [
            self._resolve_module_qualname(path, repo=repo, commit=commit)
            for path in sorted(set(import_paths))
        ]
        imported_targets = sorted(
            {
                str(result["target_entity_id"])
                for result in resolved_imports
                if result.get("status") == "RESOLVED_UNIQUE"
            }
        )
        if len(imported_targets) == 1:
            return self._resolved(
                imported_targets[0],
                "unique_import_attribute",
                binding_scope_id=binding_scope_id,
                import_paths=sorted(set(import_paths)),
            )
        if len(imported_targets) > 1:
            return self._rejected(
                "AMBIGUOUS_IMPORTED_ATTRIBUTE",
                expression=shape.get("text"),
                candidates=imported_targets,
            )

        if len(candidates) == 1:
            target = self.entities[candidates[0]]
            if target.get("kind") == "class":
                return self._class_member(candidates[0], attrs, "lexical_class_member")
            if target.get("kind") == "module":
                module_name = target.get("module_name")
                if module_name:
                    return self._resolve_module_qualname(
                        ".".join([str(module_name), *attrs]),
                        repo=repo,
                        commit=commit,
                    )
        if len(candidates) > 1:
            return self._rejected(
                "AMBIGUOUS_ATTRIBUTE_ROOT",
                expression=shape.get("text"),
                candidates=candidates,
            )
        return self._rejected("DYNAMIC_OR_UNRESOLVED_ATTRIBUTE", expression=shape.get("text"))

    def _expression_certificate_rejection(
        self,
        *,
        scope_id: str,
        shape: Mapping[str, object],
        result: Mapping[str, object],
    ) -> dict[str, object] | None:
        """Enforce the intentionally narrow, machine-checkable certificate core.

        Candidate discovery remains broader so coarse baselines can inspect
        rejected targets.  Only this small subset can become CERTIFIED:
        expressions in an undecorated unconditional module-top-level
        function, using a simple Name bound in that module, and targeting an
        undecorated, unconditional module-top-level entity.  Attribute lookup
        is candidate-only because Python permits alias and target mutation
        through channels this index deliberately does not model.
        """

        scope = self.scopes[scope_id]
        source_owner = self.entities[str(scope["owner_entity_id"])]
        proof = dict(result.get("proof", {}))
        strategy = str(proof.get("strategy", ""))
        if strategy == "same_class_receiver":
            return self._rejected(
                "NOMINAL_SELF_MEMBER",
                expression=shape.get("text"),
                static_candidates=[str(result["target_entity_id"])],
                target_entity_id=str(result["target_entity_id"]),
            )

        source_allowed = False
        if scope.get("kind") == "function":
            parent_id = source_owner.get("parent_scope_id")
            parent = self.scopes.get(str(parent_id)) if parent_id else None
            source_allowed = bool(
                parent
                and parent.get("kind") == "module"
                and source_owner.get("kind") in {"function", "async_function"}
                and source_owner.get("definition_certainty") == "unconditional_syntax"
                and not source_owner.get("decorators")
                and self._entity_binding_rejection(str(source_owner["entity_id"])) is None
            )
        if not source_allowed:
            return self._rejected(
                "SOURCE_SCOPE_OUTSIDE_CONSERVATIVE_CERTIFICATE",
                expression=shape.get("text"),
                static_candidates=[str(result["target_entity_id"])],
                source_scope_kind=scope.get("kind"),
                source_entity_id=source_owner.get("entity_id"),
            )

        target_id = str(result["target_entity_id"])
        target = self.entities[target_id]
        target_parent_id = target.get("parent_scope_id")
        target_parent = self.scopes.get(str(target_parent_id)) if target_parent_id else None
        if not (
            target_parent
            and target_parent.get("kind") == "module"
            and target.get("kind") in {"function", "async_function"}
            and target.get("definition_certainty") == "unconditional_syntax"
            and not target.get("decorators")
        ):
            return self._rejected(
                "TARGET_OUTSIDE_CONSERVATIVE_CERTIFICATE",
                expression=shape.get("text"),
                static_candidates=[target_id],
                target_entity_id=target_id,
            )

        attrs = [str(item) for item in shape.get("attrs", [])]
        if not attrs:
            binding_scope_id = proof.get("binding_scope_id")
            binding_scope = self.scopes.get(str(binding_scope_id)) if binding_scope_id else None
            bucket, _ = self._bucket_lookup(scope_id, str(shape.get("root")))
            definitions = [str(item["entity_id"]) for item in bucket.get("definitions", [])] if bucket else []
            if (
                strategy == "lexical_unique_binding"
                and binding_scope
                and binding_scope.get("kind") == "module"
                and bucket is not None
                and definitions == [target_id]
                and not bucket.get("imports")
                and not any(int(value) for value in dict(bucket.get("blocker_counts", {})).values())
                and source_owner.get("module_name") == target.get("module_name")
            ):
                return None
            return self._rejected(
                "IMPORTED_OR_NONLOCAL_SYMBOL_OUTSIDE_CONSERVATIVE_CERTIFICATE",
                expression=shape.get("text"),
                static_candidates=[target_id],
                strategy=strategy,
            )

        return self._rejected(
            "ATTRIBUTE_LOOKUP_OUTSIDE_CONSERVATIVE_CERTIFICATE",
            expression=shape.get("text"),
            static_candidates=[target_id],
            strategy=strategy,
        )

    def resolve_expression(
        self,
        scope_id: str,
        shape: Mapping[str, object],
        *,
        lineno: int | None,
        col_offset: int | None,
    ) -> dict[str, object]:
        result = self._resolve_expression_candidate(
            scope_id,
            shape,
            lineno=lineno,
            col_offset=col_offset,
        )
        if result.get("status") != "RESOLVED_UNIQUE":
            return result
        rejection = self._expression_certificate_rejection(
            scope_id=scope_id,
            shape=shape,
            result=result,
        )
        return rejection or result


class SnapshotBuilder:
    def __init__(
        self,
        *,
        repo: str,
        commit: str,
        paths: Sequence[str],
        emit_entity: Callable[[Mapping[str, object]], None],
        emit_scope: Callable[[Mapping[str, object]], None],
        emit_edge: Callable[[Mapping[str, object]], None],
        emit_site: Callable[[Mapping[str, object]], None],
        emit_witness: Callable[[Mapping[str, object]], None],
        ledger: RejectionLedger,
    ) -> None:
        self.repo = repo
        self.commit = commit
        self.module_names = _module_names(paths)
        self.emit_entity = emit_entity
        self.emit_scope = emit_scope
        self._edge_sink = emit_edge
        self._site_sink = emit_site
        self._witness_sink = emit_witness
        self.ledger = ledger
        self.entities: list[dict[str, object]] = []
        self.scopes: dict[str, ScopeState] = {}
        self._edge_aggregates: dict[str, dict[str, object]] = {}
        self._site_aggregates: dict[str, dict[str, object]] = {}
        self._sites_by_id: dict[str, dict[str, object]] = {}
        self._site_witnesses: dict[str, list[dict[str, object]]] = defaultdict(list)
        self.raw_edge_occurrences = 0
        self.raw_site_occurrences = 0
        self.fact_file = tempfile.TemporaryFile(mode="w+t", encoding="utf-8", newline="\n")
        self.python_bytes = 0
        self.python_files = 0

    def _aggregate_site(self, record: Mapping[str, object]) -> str:
        occurrence_count = int(record.get("occurrence_count", 1))
        if occurrence_count < 1:
            raise ValueError("site occurrence_count must be positive")
        self.raw_site_occurrences += occurrence_count
        witness = dict(record["witness"])
        identity = {
            "repo": record["repo"],
            "commit": record["commit"],
            "operation": record["operation"],
            "source_entity_id": record["source_entity_id"],
            "scope_id": record["scope_id"],
            "resolution_status": record["resolution_status"],
            "candidate_entity_ids": record["candidate_entity_ids"],
            "reason": record.get("reason"),
            "proof": record.get("proof"),
            "expression": witness.get("expression"),
        }
        key = canonical_json(identity)
        site_id = "pysite:v1:" + hashlib.sha256(key.encode("utf-8")).hexdigest()
        raw_witnesses = record.get("occurrence_witnesses")
        if raw_witnesses is None:
            raw_witnesses = [witness]
        witnesses = [_compact_witness(item) for item in raw_witnesses]
        if len(witnesses) != occurrence_count:
            raise ValueError("site witness rows do not conserve occurrence_count")
        self._site_witnesses[key].extend(witnesses)
        existing = self._site_aggregates.get(key)
        if existing is None:
            stored = {
                field_name: field_value
                for field_name, field_value in record.items()
                if field_name not in {"occurrence_witnesses", "last_witness"}
            }
            stored["site_id"] = site_id
            stored["occurrence_count"] = occurrence_count
            self._site_aggregates[key] = stored
            self._sites_by_id[site_id] = stored
            return site_id
        existing["occurrence_count"] = int(existing["occurrence_count"]) + occurrence_count
        return site_id

    def _aggregate_edge(self, record: Mapping[str, object]) -> None:
        site_id = record.get("resolution_site_id")
        if not site_id:
            raise ValueError("every relation edge must reference a resolution site")
        site = self._sites_by_id.get(str(site_id))
        if site is None:
            raise ValueError("relation edge references an unknown resolution site")
        if record.get("source_entity_id") != site.get("source_entity_id"):
            raise ValueError("relation edge/source site mismatch")
        if record.get("resolution_status") != site.get("resolution_status"):
            raise ValueError("relation edge/site status mismatch")
        if str(record.get("target_entity_id")) not in {
            str(item) for item in site.get("candidate_entity_ids", [])
        }:
            raise ValueError("relation edge target is not a site candidate")
        occurrence_count = int(record.get("occurrence_count", 1))
        if occurrence_count < 1:
            raise ValueError("edge occurrence_count must be positive")
        self.raw_edge_occurrences += occurrence_count
        witness = dict(record["witness"])
        identity = {
            "edge_type": record["edge_type"],
            "resolution_status": record["resolution_status"],
            "source_entity_id": record["source_entity_id"],
            "target_entity_id": record["target_entity_id"],
            "resolution_site_id": record.get("resolution_site_id"),
            "expression": witness.get("expression"),
            "resolver": witness.get("resolver"),
            "resolver_rejection_reason": witness.get("resolver_rejection_reason"),
        }
        key = canonical_json(identity)
        existing = self._edge_aggregates.get(key)
        if existing is None:
            stored = dict(record)
            stored["edge_id"] = "pyedge:v1:" + hashlib.sha256(key.encode("utf-8")).hexdigest()
            stored["occurrence_count"] = occurrence_count
            self._edge_aggregates[key] = stored
            return
        existing["occurrence_count"] = int(existing["occurrence_count"]) + occurrence_count

    def _flush_canonical_relations(self) -> None:
        entities = {str(item["entity_id"]): item for item in self.entities}
        edge_targets_by_site: dict[str, set[str]] = defaultdict(set)
        for edge in self._edge_aggregates.values():
            source_id = str(edge["source_entity_id"])
            target_id = str(edge["target_entity_id"])
            if source_id not in entities or target_id not in entities:
                raise ValueError("relation edge endpoint is missing from the entity table")
            source = entities[source_id]
            target = entities[target_id]
            if (source["repo"], source["commit"]) != (target["repo"], target["commit"]):
                raise ValueError("relation edge crosses snapshot partitions")
            edge_targets_by_site[str(edge["resolution_site_id"])].add(target_id)
        for site in self._site_aggregates.values():
            candidates = {str(item) for item in site.get("candidate_entity_ids", [])}
            linked = edge_targets_by_site.get(str(site["site_id"]), set())
            if candidates != linked:
                raise ValueError("resolution-site candidate/edge target conservation failed")
        for key in sorted(self._site_aggregates):
            site = self._site_aggregates[key]
            self._site_sink(site)
            witnesses = sorted(
                self._site_witnesses[key],
                key=lambda item: (
                    str(item.get("path", "")),
                    int(item.get("lineno", 0)),
                    int(item.get("col_offset", 0)),
                    int(item.get("end_lineno", 0)),
                    int(item.get("end_col_offset", 0)),
                    str(item.get("expression", "")),
                ),
            )
            if len(witnesses) != int(site["occurrence_count"]):
                raise ValueError("canonical site witness conservation failed")
            for ordinal, witness in enumerate(witnesses, start=1):
                self._witness_sink(
                    {
                        "schema_version": SCHEMA_VERSION,
                        "site_id": site["site_id"],
                        "witness_ordinal": ordinal,
                        **witness,
                    }
                )
        for key in sorted(self._edge_aggregates):
            self._edge_sink(self._edge_aggregates[key])

    def _emit_resolution_site(
        self,
        *,
        operation: str,
        source_entity_id: str,
        scope_id: str,
        witness: Mapping[str, object],
        result: Mapping[str, object],
        occurrence_count: int = 1,
        occurrence_witnesses: Sequence[Mapping[str, object]] | None = None,
    ) -> tuple[str, list[str], str]:
        resolution_class = _resolution_class(result)
        candidates = _candidate_ids(result)
        site_id = self._aggregate_site(
            {
                "schema_version": SCHEMA_VERSION,
                "repo": self.repo,
                "commit": self.commit,
                "operation": operation,
                "source_entity_id": source_entity_id,
                "scope_id": scope_id,
                "resolution_status": resolution_class,
                "candidate_entity_ids": candidates,
                "reason": result.get("reason"),
                "proof": result.get("proof"),
                "witness": dict(witness),
                "occurrence_count": occurrence_count,
                **(
                    {"occurrence_witnesses": [dict(item) for item in occurrence_witnesses]}
                    if occurrence_witnesses is not None
                    else {}
                ),
            }
        )
        return resolution_class, candidates, site_id

    def _emit_candidate_edges(
        self,
        *,
        edge_type: str,
        source_entity_id: str,
        candidate_ids: Sequence[str],
        resolution_status: str,
        witness: Mapping[str, object],
        reason: str,
        occurrence_count: int = 1,
        resolution_site_id: str | None = None,
    ) -> None:
        for target_id in sorted(set(candidate_ids)):
            self._aggregate_edge(
                {
                    "schema_version": SCHEMA_VERSION,
                    "edge_type": edge_type,
                    "resolution_status": resolution_status,
                    "source_entity_id": source_entity_id,
                    "target_entity_id": target_id,
                    "witness": {**dict(witness), "resolver_rejection_reason": reason},
                    "occurrence_count": occurrence_count,
                    **({"resolution_site_id": resolution_site_id} if resolution_site_id else {}),
                }
            )

    def add_source(self, path: str, blob_oid: str, data: bytes) -> None:
        text, _encoding = _decode_python(data)
        try:
            FactExtractor(
                repo=self.repo,
                commit=self.commit,
                path=path,
                blob_oid=blob_oid,
                text=text,
                module_name=self.module_names[path],
                entities=self.entities,
                scopes=self.scopes,
                fact_handle=self.fact_file,
            )
        except SyntaxError as error:
            raise RuntimeError(f"full Python blob failed AST parse: {self.repo}@{self.commit}:{path}: {error}") from error
        self.python_bytes += len(data)
        self.python_files += 1

    def _entity_maps(self) -> tuple[dict[str, dict[str, object]], dict[str, list[str]], dict[tuple[str, str], list[str]]]:
        entities = {str(item["entity_id"]): item for item in self.entities}
        modules: dict[str, list[str]] = defaultdict(list)
        module_quals: dict[tuple[str, str], list[str]] = defaultdict(list)
        for entity in self.entities:
            module_name = entity.get("module_name")
            if not module_name:
                continue
            if entity["kind"] == "module":
                modules[str(module_name)].append(str(entity["entity_id"]))
            else:
                module_quals[(str(module_name), str(entity["qualname"]))].append(str(entity["entity_id"]))
        return entities, modules, module_quals

    def _reject_import_binding(
        self,
        *,
        scope_id: str,
        binding: dict[str, object],
        target_ids: Sequence[str],
        reason: str,
    ) -> None:
        binding["resolution_status"] = "REJECTED"
        binding["rejection_reason"] = reason
        binding["candidate_entity_ids"] = sorted(set(target_ids))
        witness = {
            "path": binding["path"],
            "blob_oid": binding["blob_oid"],
            "lineno": binding["lineno"],
            "col_offset": binding["col_offset"],
            "end_lineno": binding["end_lineno"],
            "expression": binding.get("canonical_symbol"),
            "scope_id": scope_id,
        }
        resolution_status, candidates, site_id = self._emit_resolution_site(
            operation="IMPORTS_OF",
            source_entity_id=str(binding["owner_entity_id"]),
            scope_id=scope_id,
            witness=witness,
            result={
                "status": "REJECTED",
                "reason": reason,
                "static_candidates": sorted(set(target_ids)),
            },
        )
        self._emit_candidate_edges(
            edge_type=EDGE_IMPORTS,
            source_entity_id=str(binding["owner_entity_id"]),
            candidate_ids=candidates,
            resolution_status=resolution_status,
            witness=witness,
            reason=reason,
            resolution_site_id=site_id,
        )
        self.ledger.add(
            "IMPORTS_OF",
            reason,
            {
                "repo": self.repo,
                "commit": self.commit,
                "scope_id": scope_id,
                "path": binding["path"],
                "lineno": binding["lineno"],
                "candidates": sorted(set(target_ids)),
            },
        )

    def _resolve_imports(self) -> list[dict[str, object]]:
        entities, modules, module_quals = self._entity_maps()
        stability_resolver = Resolver(
            entities,
            {scope_id: state.to_record() for scope_id, state in self.scopes.items()},
        )
        import_edges: list[dict[str, object]] = []
        for scope_id in sorted(self.scopes):
            scope = self.scopes[scope_id]
            for bound_name in sorted(scope.bindings):
                bucket = scope.bindings[bound_name]
                for binding in bucket.imports:
                    target_ids: list[str] = []
                    if binding["style"] == "import":
                        imported_module = str(binding["imported_module"])
                        target_ids = list(modules.get(imported_module, []))
                        binding["canonical_symbol"] = imported_module
                        reason = "EXTERNAL_OR_UNRESOLVED_MODULE"
                    else:
                        imported_name = str(binding["imported_name"])
                        base = _relative_module(
                            scope.module_name,
                            scope.path,
                            str(binding["module"]) if binding.get("module") else None,
                            int(binding.get("level", 0)),
                        )
                        binding["resolved_from_module"] = base
                        if imported_name == "*":
                            binding["resolution_status"] = "REJECTED"
                            binding["rejection_reason"] = "STAR_IMPORT_DYNAMIC_NAMESPACE"
                            witness = {
                                "path": binding["path"],
                                "blob_oid": binding["blob_oid"],
                                "lineno": binding["lineno"],
                                "col_offset": binding["col_offset"],
                                "end_lineno": binding["end_lineno"],
                                "expression": "*",
                            }
                            self._emit_resolution_site(
                                operation="IMPORTS_OF",
                                source_entity_id=str(binding["owner_entity_id"]),
                                scope_id=scope_id,
                                witness=witness,
                                result={"status": "REJECTED", "reason": "STAR_IMPORT_DYNAMIC_NAMESPACE"},
                            )
                            self.ledger.add(
                                "IMPORTS_OF",
                                "STAR_IMPORT_DYNAMIC_NAMESPACE",
                                {
                                    "repo": self.repo,
                                    "commit": self.commit,
                                    "scope_id": scope_id,
                                    "path": binding["path"],
                                    "lineno": binding["lineno"],
                                },
                            )
                            continue
                        canonical = f"{base}.{imported_name}" if base else imported_name
                        binding["canonical_symbol"] = canonical
                        if base:
                            target_ids.extend(modules.get(canonical, []))
                            target_ids.extend(module_quals.get((base, imported_name), []))
                        reason = "EXTERNAL_OR_UNRESOLVED_FROM_IMPORT"
                    target_ids = sorted(set(target_ids))
                    if binding.get("definition_certainty") != "unconditional_syntax":
                        self._reject_import_binding(
                            scope_id=scope_id,
                            binding=binding,
                            target_ids=target_ids,
                            reason="CONDITIONAL_BINDING_NOT_DOMINATING",
                        )
                        continue
                    certificate_reason: str | None = None
                    if scope.kind != "module":
                        certificate_reason = "IMPORT_SCOPE_OUTSIDE_CONSERVATIVE_CERTIFICATE"
                    elif scope.scope_poison_reasons or bound_name in scope.poisoned_names:
                        certificate_reason = "IMPORT_SOURCE_SCOPE_POISONED"
                    elif len(bucket.imports) > 1:
                        certificate_reason = "AMBIGUOUS_IMPORT_BINDING"
                    elif (
                        bucket.definitions
                        or sum(bucket.blocker_counts.values())
                        or len(bucket.imports) != 1
                    ):
                        certificate_reason = "IMPORT_BINDING_DYNAMIC_OR_REBOUND"
                    elif len(target_ids) == 1:
                        target = entities[target_ids[0]]
                        if target.get("kind") != "module":
                            parent_id = target.get("parent_scope_id")
                            parent = stability_resolver.scopes.get(str(parent_id)) if parent_id else None
                            if parent is None or parent.get("kind") != "module":
                                certificate_reason = "TARGET_OUTSIDE_CONSERVATIVE_CERTIFICATE"
                            else:
                                certificate_reason = stability_resolver._entity_binding_rejection(target_ids[0])
                            if certificate_reason is None:
                                certificate_reason = "IMPORTED_SYMBOL_OUTSIDE_CONSERVATIVE_CERTIFICATE"
                        elif binding.get("style") != "import":
                            certificate_reason = "MODULE_TARGET_REQUIRES_DIRECT_IMPORT_SYNTAX"
                    if certificate_reason is not None:
                        self._reject_import_binding(
                            scope_id=scope_id,
                            binding=binding,
                            target_ids=target_ids,
                            reason=certificate_reason,
                        )
                        continue
                    if len(target_ids) == 1:
                        target_id = target_ids[0]
                        import_strategy = "SOURCE_SYNTAX_MODULE_IMPORT"
                        binding["resolution_status"] = "RESOLVED_UNIQUE"
                        binding["target_entity_id"] = target_id
                        import_edges.append(
                            {
                                "schema_version": SCHEMA_VERSION,
                                "edge_type": EDGE_IMPORTS,
                                "resolution_status": "CERTIFIED",
                                "source_entity_id": binding["owner_entity_id"],
                                "target_entity_id": target_id,
                                "witness": {
                                    "path": binding["path"],
                                    "blob_oid": binding["blob_oid"],
                                    "lineno": binding["lineno"],
                                    "col_offset": binding["col_offset"],
                                    "end_lineno": binding["end_lineno"],
                                    "expression": binding["canonical_symbol"],
                                    "resolver": import_strategy,
                                    "scope_id": scope_id,
                                },
                            }
                        )
                        _status, _candidates, site_id = self._emit_resolution_site(
                            operation="IMPORTS_OF",
                            source_entity_id=str(binding["owner_entity_id"]),
                            scope_id=scope_id,
                            witness={
                                "path": binding["path"],
                                "blob_oid": binding["blob_oid"],
                                "lineno": binding["lineno"],
                                "col_offset": binding["col_offset"],
                                "end_lineno": binding["end_lineno"],
                                "expression": binding["canonical_symbol"],
                            },
                            result={
                                "status": "RESOLVED_UNIQUE",
                                "target_entity_id": target_id,
                                "proof": {"strategy": import_strategy},
                            },
                        )
                        import_edges[-1]["resolution_site_id"] = site_id
                    elif len(target_ids) > 1:
                        binding["resolution_status"] = "REJECTED"
                        binding["rejection_reason"] = "AMBIGUOUS_IMPORT_TARGET"
                        binding["candidate_entity_ids"] = target_ids
                        witness = {
                            "path": binding["path"],
                            "blob_oid": binding["blob_oid"],
                            "lineno": binding["lineno"],
                            "col_offset": binding["col_offset"],
                            "end_lineno": binding["end_lineno"],
                            "expression": binding.get("canonical_symbol"),
                            "scope_id": scope_id,
                        }
                        resolution_status, candidates, site_id = self._emit_resolution_site(
                            operation="IMPORTS_OF",
                            source_entity_id=str(binding["owner_entity_id"]),
                            scope_id=scope_id,
                            witness=witness,
                            result={
                                "status": "REJECTED",
                                "reason": "AMBIGUOUS_IMPORT_TARGET",
                                "candidates": target_ids,
                            },
                        )
                        self._emit_candidate_edges(
                            edge_type=EDGE_IMPORTS,
                            source_entity_id=str(binding["owner_entity_id"]),
                            candidate_ids=candidates,
                            resolution_status=resolution_status,
                            witness=witness,
                            reason="AMBIGUOUS_IMPORT_TARGET",
                            resolution_site_id=site_id,
                        )
                        self.ledger.add(
                            "IMPORTS_OF",
                            "AMBIGUOUS_IMPORT_TARGET",
                            {
                                "repo": self.repo,
                                "commit": self.commit,
                                "scope_id": scope_id,
                                "path": binding["path"],
                                "lineno": binding["lineno"],
                                "canonical_symbol": binding.get("canonical_symbol"),
                                "candidates": target_ids,
                            },
                        )
                    else:
                        binding["resolution_status"] = "REJECTED"
                        binding["rejection_reason"] = reason
                        self._emit_resolution_site(
                            operation="IMPORTS_OF",
                            source_entity_id=str(binding["owner_entity_id"]),
                            scope_id=scope_id,
                            witness={
                                "path": binding["path"],
                                "blob_oid": binding["blob_oid"],
                                "lineno": binding["lineno"],
                                "col_offset": binding["col_offset"],
                                "end_lineno": binding["end_lineno"],
                                "expression": binding.get("canonical_symbol"),
                            },
                            result={"status": "REJECTED", "reason": reason},
                        )
                        self.ledger.add(
                            "IMPORTS_OF",
                            reason,
                            {
                                "repo": self.repo,
                                "commit": self.commit,
                                "scope_id": scope_id,
                                "path": binding["path"],
                                "lineno": binding["lineno"],
                                "canonical_symbol": binding.get("canonical_symbol"),
                            },
                        )
        return sorted(import_edges, key=canonical_json)

    def _fixture_decorator(self, entity: Mapping[str, object], resolver: Resolver) -> dict[str, object]:
        parent_scope_id = str(entity["parent_scope_id"])
        for decorator in entity.get("decorators", []):
            shape = decorator["shape"]
            root = str(shape.get("root"))
            attrs = [str(item) for item in shape.get("attrs", [])]
            syntactic_fixture = (
                (attrs == ["fixture"])
                or (not attrs and str(shape.get("text", "")).endswith("fixture"))
            )
            if not syntactic_fixture:
                continue
            parent_scope = resolver.scopes[parent_scope_id]
            if parent_scope.get("kind") == "function":
                return {
                    "status": "REJECTED",
                    "reason": "PYTEST_NESTED_NOT_COLLECTIBLE",
                    "decorator": decorator,
                }
            if parent_scope.get("kind") != "module":
                return {
                    "status": "REJECTED",
                    "reason": "PYTEST_NESTED_NOT_COLLECTIBLE",
                    "decorator": decorator,
                }
            if entity.get("definition_certainty") != "unconditional_syntax":
                return {
                    "status": "REJECTED",
                    "reason": "CONDITIONAL_BINDING_NOT_DOMINATING",
                    "decorator": decorator,
                }
            bucket, _ = resolver._bucket_lookup(parent_scope_id, root)
            if bucket is None:
                return {
                    "status": "REJECTED",
                    "reason": "UNRESOLVED_PYTEST_FIXTURE_DECORATOR",
                    "decorator": decorator,
                }
            blocker_total = sum(int(value) for value in dict(bucket.get("blocker_counts", {})).values())
            if blocker_total:
                return {
                    "status": "REJECTED",
                    "reason": "PYTEST_DECORATOR_BINDING_REBOUND",
                    "decorator": decorator,
                }
            definitions = list(bucket.get("definitions", []))
            imports = list(bucket.get("imports", []))
            matching: list[Mapping[str, object]] = []
            for binding in imports:
                canonical = str(binding.get("canonical_symbol", ""))
                if binding.get("style") == "import" and canonical == "pytest" and attrs == ["fixture"]:
                    matching.append(binding)
                if binding.get("style") == "from" and canonical == "pytest.fixture" and not attrs:
                    matching.append(binding)
            competing_imports = [item for item in imports if item not in matching]
            if len(matching) != 1 or definitions or competing_imports:
                return {
                    "status": "REJECTED",
                    "reason": "AMBIGUOUS_PYTEST_FIXTURE_DECORATOR",
                    "decorator": decorator,
                }
            if len(entity.get("decorators", [])) != 1:
                return {
                    "status": "REJECTED",
                    "reason": "FIXTURE_DECORATOR_STACK_UNCERTAIN",
                    "decorator": decorator,
                }
            return {
                "status": "REJECTED",
                "reason": "PYTEST_FIXTURE_COLLECTION_OUTSIDE_CONSERVATIVE_CERTIFICATE",
                "fixture_name": decorator.get("name_override") or str(entity.get("name")),
                "decorator": decorator,
            }
        return {"status": "NOT_APPLICABLE"}

    @staticmethod
    def _test_role(entity: Mapping[str, object], resolver: Resolver) -> dict[str, object]:
        if entity.get("kind") not in {"function", "async_function"}:
            return {"status": "NOT_APPLICABLE"}
        name = str(entity.get("name", ""))
        if not name.startswith("test_"):
            return {"status": "NOT_APPLICABLE"}
        path = PurePosixPath(str(entity["path"]))
        if not (path.name.startswith("test_") or any(part in {"test", "tests", "testing"} for part in path.parts)):
            return {"status": "NOT_APPLICABLE"}
        parent_scope = resolver.scopes[str(entity["parent_scope_id"])]
        if parent_scope.get("kind") == "module":
            if "__test__" in dict(parent_scope.get("bindings", {})):
                return {"status": "REJECTED", "reason": "PYTEST_MODULE_TEST_FLAG_UNCERTAIN"}
        else:
            return {"status": "REJECTED", "reason": "PYTEST_NESTED_NOT_COLLECTIBLE"}
        if entity.get("definition_certainty") != "unconditional_syntax":
            return {"status": "REJECTED", "reason": "CONDITIONAL_BINDING_NOT_DOMINATING"}
        if entity.get("decorators"):
            return {"status": "REJECTED", "reason": "DECORATED_BINDING_MAY_REPLACE"}
        binding_rejection = resolver._entity_binding_rejection(str(entity["entity_id"]))
        if binding_rejection is not None:
            return {"status": "REJECTED", "reason": binding_rejection}
        return {"status": "CERTIFIED"}

    def _fixture_edges(self, resolver: Resolver) -> list[dict[str, object]]:
        fixture_by_name: dict[str, list[dict[str, object]]] = defaultdict(list)
        test_ids: set[str] = set()
        fixture_ids: set[str] = set()
        role_edges: list[dict[str, object]] = []
        for entity in sorted(self.entities, key=lambda item: str(item["entity_id"])):
            entity_id = str(entity["entity_id"])
            test_role = self._test_role(entity, resolver)
            test_witness = {
                "path": entity["path"],
                "blob_oid": entity["blob_oid"],
                "lineno": entity["lineno"],
                "end_lineno": entity["end_lineno"],
                "expression": entity.get("name"),
                "resolver": "pytest_test_name_and_path_convention",
            }
            if test_role["status"] == "CERTIFIED":
                test_ids.add(entity_id)
                role_edges.append(
                    {
                        "schema_version": SCHEMA_VERSION,
                        "edge_type": EDGE_AS_TEST,
                        "resolution_status": "CERTIFIED",
                        "source_entity_id": entity_id,
                        "target_entity_id": entity_id,
                        "witness": test_witness,
                    }
                )
                _status, _candidates, site_id = self._emit_resolution_site(
                    operation="AS_TEST",
                    source_entity_id=entity_id,
                    scope_id=str(entity.get("scope_id")),
                    witness=role_edges[-1]["witness"],
                    result={
                        "status": "RESOLVED_UNIQUE",
                        "target_entity_id": entity_id,
                        "proof": {"strategy": "pytest_test_name_and_path_convention"},
                    },
                )
                role_edges[-1]["resolution_site_id"] = site_id
            elif test_role["status"] == "REJECTED":
                self._emit_resolution_site(
                    operation="AS_TEST",
                    source_entity_id=entity_id,
                    scope_id=str(entity.get("scope_id")),
                    witness=test_witness,
                    result={"status": "REJECTED", "reason": test_role["reason"]},
                )
                self.ledger.add(
                    "AS_TEST",
                    str(test_role["reason"]),
                    {
                        "repo": self.repo,
                        "commit": self.commit,
                        "source_entity_id": entity_id,
                        "witness": test_witness,
                    },
                )

            fixture_role = self._fixture_decorator(entity, resolver)
            if fixture_role["status"] == "CERTIFIED":
                fixture_name = str(fixture_role["fixture_name"])
                decorator = fixture_role["decorator"]
                fixture_ids.add(entity_id)
                fixture_by_name[fixture_name].append(entity)
                role_edges.append(
                    {
                        "schema_version": SCHEMA_VERSION,
                        "edge_type": EDGE_AS_FIXTURE,
                        "resolution_status": "CERTIFIED",
                        "source_entity_id": entity_id,
                        "target_entity_id": entity_id,
                        "witness": {
                            **decorator["witness"],
                            "expression": decorator["shape"]["text"],
                            "fixture_name": fixture_name,
                            "resolver": "explicit_pytest_fixture_import_and_decorator",
                        },
                    }
                )
                _status, _candidates, site_id = self._emit_resolution_site(
                    operation="AS_FIXTURE",
                    source_entity_id=entity_id,
                    scope_id=str(entity.get("scope_id")),
                    witness=role_edges[-1]["witness"],
                    result={
                        "status": "RESOLVED_UNIQUE",
                        "target_entity_id": entity_id,
                        "proof": {"strategy": "explicit_pytest_fixture_import_and_decorator"},
                    },
                )
                role_edges[-1]["resolution_site_id"] = site_id
            elif fixture_role["status"] == "REJECTED":
                decorator = fixture_role["decorator"]
                visible_candidate = (
                    fixture_role["reason"]
                    == "PYTEST_FIXTURE_COLLECTION_OUTSIDE_CONSERVATIVE_CERTIFICATE"
                )
                if visible_candidate:
                    fixture_name = str(fixture_role["fixture_name"])
                    fixture_by_name[fixture_name].append(entity)
                rejected_witness = {
                    **decorator["witness"],
                    "expression": decorator["shape"]["text"],
                    "resolver": "pytest_fixture_role_rejected",
                }
                resolution_status, candidates, site_id = self._emit_resolution_site(
                    operation="AS_FIXTURE",
                    source_entity_id=entity_id,
                    scope_id=str(entity.get("scope_id")),
                    witness=rejected_witness,
                    result={
                        "status": "REJECTED",
                        "reason": fixture_role["reason"],
                        "static_candidates": [entity_id] if visible_candidate else [],
                    },
                )
                self._emit_candidate_edges(
                    edge_type=EDGE_AS_FIXTURE,
                    source_entity_id=entity_id,
                    candidate_ids=candidates,
                    resolution_status=resolution_status,
                    witness=rejected_witness,
                    reason=str(fixture_role["reason"]),
                    resolution_site_id=site_id,
                )
                self.ledger.add(
                    "AS_FIXTURE",
                    str(fixture_role["reason"]),
                    {
                        "repo": self.repo,
                        "commit": self.commit,
                        "source_entity_id": entity_id,
                        "witness": rejected_witness,
                    },
                )

        use_edges: list[dict[str, object]] = []
        entities_by_id = {str(item["entity_id"]): item for item in self.entities}
        for entity_id in sorted(test_ids):
            entity = entities_by_id[entity_id]
            parameters = list(entity.get("parameters", []))
            function_scope = self.scopes.get(str(entity.get("scope_id")))
            receiver_names = set(function_scope.receiver_names if function_scope else ())
            for parameter in parameters:
                name = str(parameter["name"])
                if name in receiver_names:
                    continue
                candidates = list(fixture_by_name.get(name, []))
                same_file = [item for item in candidates if item["path"] == entity["path"]]
                if same_file:
                    candidates = same_file
                else:
                    test_parent = PurePosixPath(str(entity["path"])).parent
                    ancestor_candidates: list[tuple[int, dict[str, object]]] = []
                    for candidate in candidates:
                        candidate_path = PurePosixPath(str(candidate["path"]))
                        if candidate_path.name != "conftest.py":
                            continue
                        candidate_parent = candidate_path.parent
                        try:
                            relative = test_parent.relative_to(candidate_parent)
                        except ValueError:
                            continue
                        ancestor_candidates.append((len(relative.parts), candidate))
                    if ancestor_candidates:
                        nearest = min(distance for distance, _ in ancestor_candidates)
                        candidates = [item for distance, item in ancestor_candidates if distance == nearest]
                    else:
                        candidates = []
                candidate_ids = sorted({str(item["entity_id"]) for item in candidates})
                witness = {
                    "path": entity["path"],
                    "blob_oid": entity["blob_oid"],
                    "lineno": parameter["lineno"],
                    "end_lineno": parameter["lineno"],
                    "expression": name,
                    "resolver": "pytest_parameter_nearest_visible_fixture",
                }
                if candidate_ids:
                    reason = (
                        "AMBIGUOUS_FIXTURE_PARAMETER"
                        if len(candidate_ids) > 1
                        else "PYTEST_FIXTURE_RUNTIME_SELECTION_OUTSIDE_CERTIFICATE"
                    )
                    resolution_status, site_candidates, site_id = self._emit_resolution_site(
                        operation="USES_FIXTURE",
                        source_entity_id=entity_id,
                        scope_id=str(entity.get("scope_id")),
                        witness=witness,
                        result={"status": "REJECTED", "reason": reason, "candidates": candidate_ids},
                    )
                    self._emit_candidate_edges(
                        edge_type=EDGE_USES_FIXTURE,
                        source_entity_id=entity_id,
                        candidate_ids=site_candidates,
                        resolution_status=resolution_status,
                        witness=witness,
                        reason=reason,
                        resolution_site_id=site_id,
                    )
                    self.ledger.add(
                        "USES_FIXTURE",
                        reason,
                        {
                            "repo": self.repo,
                            "commit": self.commit,
                            "source_entity_id": entity_id,
                            "parameter": name,
                            "candidate_entity_ids": candidate_ids,
                            "witness": witness,
                        },
                    )
                else:
                    reason = "UNRESOLVED_FIXTURE_PARAMETER"
                    self._emit_resolution_site(
                        operation="USES_FIXTURE",
                        source_entity_id=entity_id,
                        scope_id=str(entity.get("scope_id")),
                        witness=witness,
                        result={"status": "REJECTED", "reason": reason, "candidates": []},
                    )
                    self.ledger.add(
                        "USES_FIXTURE",
                        reason,
                        {
                            "repo": self.repo,
                            "commit": self.commit,
                            "source_entity_id": entity_id,
                            "parameter": name,
                            "candidate_entity_ids": [],
                            "witness": witness,
                        },
                    )
        return sorted([*role_edges, *use_edges], key=canonical_json)

    def finalize(self) -> dict[str, object]:
        import_edges = self._resolve_imports()
        entity_map = {str(item["entity_id"]): item for item in self.entities}
        scope_records = {scope_id: state.to_record() for scope_id, state in self.scopes.items()}
        resolver = Resolver(entity_map, scope_records)
        fixture_edges = self._fixture_edges(resolver)

        for entity in sorted(self.entities, key=lambda item: str(item["entity_id"])):
            self.emit_entity(_public_entity(entity))
        for scope_id in sorted(self.scopes):
            self.emit_scope(self.scopes[scope_id].to_record())
        for edge in [*import_edges, *fixture_edges]:
            self._aggregate_edge(edge)

        expression_counts: Counter[str] = Counter()
        resolved_counts: Counter[str] = Counter()
        self.fact_file.seek(0)
        for line in self.fact_file:
            fact = json.loads(line)
            operation = str(fact["operation"])
            occurrence_count = int(fact.get("occurrence_count", 1))
            expression_counts[operation] += occurrence_count
            shape = fact["shape"]
            result = resolver.resolve_expression(
                str(fact["scope_id"]),
                shape,
                lineno=int(fact["witness"].get("lineno", 0)),
                col_offset=int(fact["witness"].get("col_offset", 0)),
            )
            edge_type = EDGE_CALLS if operation == "CALLEES_OF" else EDGE_REFS
            if (
                result["status"] == "RESOLVED_UNIQUE"
                and operation == "CALLEES_OF"
                and entity_map[str(result["target_entity_id"])]["kind"] == "module"
            ):
                result = {
                    "status": "REJECTED",
                    "reason": "MODULE_NOT_CALLABLE",
                    "candidates": [str(result["target_entity_id"])],
                }
            resolution_status, candidates, site_id = self._emit_resolution_site(
                operation=operation,
                source_entity_id=str(fact["owner_entity_id"]),
                scope_id=str(fact["scope_id"]),
                witness=fact["witness"],
                result=result,
                occurrence_count=occurrence_count,
                occurrence_witnesses=fact.get("occurrence_witnesses"),
            )
            if result["status"] != "RESOLVED_UNIQUE":
                self._emit_candidate_edges(
                    edge_type=edge_type,
                    source_entity_id=str(fact["owner_entity_id"]),
                    candidate_ids=candidates,
                    resolution_status=resolution_status,
                    witness={**fact["witness"], "scope_id": fact["scope_id"]},
                    reason=str(result["reason"]),
                    occurrence_count=occurrence_count,
                    resolution_site_id=site_id,
                )
                self.ledger.add(
                    operation,
                    str(result["reason"]),
                    {
                        "repo": self.repo,
                        "commit": self.commit,
                        "scope_id": fact["scope_id"],
                        "owner_entity_id": fact["owner_entity_id"],
                        "witness": fact["witness"],
                        "resolution": result,
                    },
                    occurrence_count=occurrence_count,
                )
                continue
            target_id = str(result["target_entity_id"])
            self._aggregate_edge(
                {
                    "schema_version": SCHEMA_VERSION,
                    "edge_type": edge_type,
                    "resolution_status": "CERTIFIED",
                    "source_entity_id": fact["owner_entity_id"],
                    "target_entity_id": target_id,
                    "witness": {
                        **fact["witness"],
                        "scope_id": fact["scope_id"],
                        "resolver": result["proof"],
                    },
                    "occurrence_count": occurrence_count,
                    "resolution_site_id": site_id,
                }
            )
            resolved_counts[operation] += occurrence_count
        self.fact_file.close()
        self._flush_canonical_relations()
        return {
            "repo": self.repo,
            "base_commit": self.commit,
            "python_file_count": self.python_files,
            "python_bytes_read": self.python_bytes,
            "entity_count": len(self.entities),
            "scope_count": len(self.scopes),
            "raw_resolution_site_occurrences": self.raw_site_occurrences,
            "canonical_resolution_site_rows": len(self._site_aggregates),
            "raw_relation_edge_occurrences": self.raw_edge_occurrences,
            "canonical_relation_edge_rows": len(self._edge_aggregates),
            "expression_sites": dict(sorted(expression_counts.items())),
            "resolved_expression_sites": dict(sorted(resolved_counts.items())),
        }


class JsonlWriter:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.temporary = path.with_name(path.name + ".tmp")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.temporary.open("w", encoding="utf-8", newline="\n")
        self.digest = hashlib.sha256()
        self.rows = 0
        self.relation_counts: Counter[str] = Counter()
        self.resolution_status_counts: Counter[str] = Counter()

    def write(self, record: Mapping[str, object]) -> None:
        encoded = (canonical_json(record) + "\n").encode("utf-8")
        self.handle.write(encoded.decode("utf-8"))
        self.digest.update(encoded)
        self.rows += 1
        if record.get("edge_type"):
            self.relation_counts[str(record["edge_type"])] += 1
        if record.get("resolution_status"):
            self.resolution_status_counts[str(record["resolution_status"])] += 1

    def close(self) -> dict[str, object]:
        self.handle.close()
        os.replace(self.temporary, self.path)
        return {
            "filename": self.path.name,
            "rows": self.rows,
            "sha256": self.digest.hexdigest(),
            "bytes": self.path.stat().st_size,
        }


def build_from_source_mapping(
    *,
    repo: str,
    commit: str,
    sources: Mapping[str, bytes | str],
) -> dict[str, object]:
    """Build an in-memory synthetic fixture without touching benchmark data."""

    entities: list[dict[str, object]] = []
    scopes: list[dict[str, object]] = []
    edges: list[dict[str, object]] = []
    sites: list[dict[str, object]] = []
    witnesses: list[dict[str, object]] = []
    ledger = RejectionLedger(examples_per_key=100)
    builder = SnapshotBuilder(
        repo=repo,
        commit=commit,
        paths=sorted(sources),
        emit_entity=lambda item: entities.append(dict(item)),
        emit_scope=lambda item: scopes.append(dict(item)),
        emit_edge=lambda item: edges.append(dict(item)),
        emit_site=lambda item: sites.append(dict(item)),
        emit_witness=lambda item: witnesses.append(dict(item)),
        ledger=ledger,
    )
    for path in sorted(sources):
        raw = sources[path]
        data = raw.encode("utf-8") if isinstance(raw, str) else raw
        oid = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        builder.add_source(path, oid, data)
    summary = builder.finalize()
    return {
        "entities": entities,
        "scopes": scopes,
        "edges": edges,
        "resolution_sites": sites,
        "resolution_witnesses": witnesses,
        "rejections": list(ledger.example_rows()),
        "rejection_counts": ledger.count_record(),
        "summary": summary,
    }


class PrimitiveLayer:
    """Minimal evidence-returning API over either in-memory or persisted rows."""

    def __init__(
        self,
        entities: Iterable[Mapping[str, object]],
        scopes: Iterable[Mapping[str, object]],
        edges: Iterable[Mapping[str, object]],
        resolution_sites: Iterable[Mapping[str, object]] = (),
        resolution_witnesses: Iterable[Mapping[str, object]] = (),
    ) -> None:
        self.entities = {str(item["entity_id"]): dict(item) for item in entities}
        self.scopes = {str(item["scope_id"]): dict(item) for item in scopes}
        self.edges = [dict(item) for item in edges]
        self.resolution_sites = [dict(item) for item in resolution_sites]
        self._resolution_witnesses = [dict(item) for item in resolution_witnesses]
        self._sites_by_source_operation: dict[tuple[str, str, str, str], list[dict[str, object]]] = defaultdict(list)
        self._witnesses_by_site: dict[str, list[dict[str, object]]] = defaultdict(list)
        for site in self.resolution_sites:
            self._sites_by_source_operation[
                (
                    str(site["repo"]),
                    str(site["commit"]),
                    str(site["source_entity_id"]),
                    str(site["operation"]),
                )
            ].append(site)
        for rows in self._sites_by_source_operation.values():
            rows.sort(key=lambda item: str(item["site_id"]))
        for witness in self._resolution_witnesses:
            self._witnesses_by_site[str(witness["site_id"])].append(witness)
        for rows in self._witnesses_by_site.values():
            rows.sort(key=lambda item: int(item["witness_ordinal"]))
        self._edge_path: Path | None = None
        self.resolver = Resolver(self.entities, self.scopes)

    @classmethod
    def from_directory(cls, index_dir: Path) -> "PrimitiveLayer":
        def rows(name: str) -> Iterator[dict[str, object]]:
            path = index_dir / name
            with path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    if line.strip():
                        yield json.loads(line)

        site_path = index_dir / "resolution_sites.jsonl"
        witness_path = index_dir / "resolution_witnesses.jsonl"
        layer = cls(
            rows("entities.jsonl"),
            rows("scopes.jsonl"),
            [],
            rows("resolution_sites.jsonl") if site_path.is_file() else (),
            rows("resolution_witnesses.jsonl") if witness_path.is_file() else (),
        )
        layer._edge_path = index_dir / "edges.jsonl"
        return layer

    def defs_at(
        self,
        *,
        path: str,
        repo: str,
        commit: str,
        lineno: int | None = None,
        name: str | None = None,
    ) -> list[dict[str, object]]:
        rows = []
        for entity in self.entities.values():
            if entity["path"] != path:
                continue
            if entity["repo"] != repo:
                continue
            if entity["commit"] != commit:
                continue
            if lineno is not None and not (int(entity["lineno"]) <= lineno <= int(entity["end_lineno"])):
                continue
            if name is not None and str(entity["qualname"]).split(".")[-1] != name:
                continue
            rows.append(entity)
        return sorted(rows, key=lambda item: (int(item["lineno"]), str(item["entity_id"])))

    def resolve_unique(
        self,
        *,
        scope_id: str,
        expression: str,
        lineno: int | None,
        col_offset: int | None,
        repo: str | None = None,
        commit: str | None = None,
    ) -> dict[str, object]:
        if scope_id not in self.scopes:
            return {"status": "REJECTED", "reason": "UNKNOWN_SCOPE_ID"}
        scope = self.scopes[scope_id]
        if repo is not None and str(scope["repo"]) != repo:
            return {"status": "REJECTED", "reason": "SCOPE_SNAPSHOT_PARTITION_MISMATCH"}
        if commit is not None and str(scope["commit"]) != commit:
            return {"status": "REJECTED", "reason": "SCOPE_SNAPSHOT_PARTITION_MISMATCH"}
        try:
            parsed = ast.parse(expression, mode="eval").body
        except SyntaxError as error:
            return {"status": "REJECTED", "reason": "INVALID_EXPRESSION_SYNTAX", "detail": str(error)}
        shape = _expression_shape(parsed)
        if shape["shape"] == "dynamic_attribute":
            return {"status": "REJECTED", "reason": "DYNAMIC_ATTRIBUTE_RECEIVER", "expression": expression}
        return self.resolver.resolve_expression(
            scope_id,
            shape,
            lineno=lineno,
            col_offset=col_offset,
        )

    def _edges(
        self,
        edge_type: str,
        field: str,
        entity_id: str,
        *,
        include_uncertified: bool = False,
    ) -> list[dict[str, object]]:
        def matches(edge: Mapping[str, object]) -> bool:
            return (
                edge["edge_type"] == edge_type
                and edge[field] == entity_id
                and (include_uncertified or edge.get("resolution_status") == "CERTIFIED")
            )

        rows = [edge for edge in self.edges if matches(edge)]
        if self._edge_path is not None:
            with self._edge_path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    if not line.strip():
                        continue
                    edge = json.loads(line)
                    if matches(edge):
                        rows.append(edge)
        return rows

    def resolution_sites_of(
        self,
        *,
        repo: str,
        commit: str,
        source_entity_id: str,
        operation: str,
        resolution_status: str | None = None,
    ) -> list[dict[str, object]]:
        rows = list(
            self._sites_by_source_operation.get(
                (repo, commit, source_entity_id, operation),
                [],
            )
        )
        if resolution_status is not None:
            rows = [item for item in rows if item["resolution_status"] == resolution_status]
        return rows

    def witnesses_for(self, site_id: str) -> list[dict[str, object]]:
        return list(self._witnesses_by_site.get(site_id, []))

    def callees_of(self, entity_id: str, *, include_uncertified: bool = False) -> list[dict[str, object]]:
        return self._edges(EDGE_CALLS, "source_entity_id", entity_id, include_uncertified=include_uncertified)

    def callers_of(self, entity_id: str, *, include_uncertified: bool = False) -> list[dict[str, object]]:
        return self._edges(EDGE_CALLS, "target_entity_id", entity_id, include_uncertified=include_uncertified)

    def imports_of(self, entity_id: str, *, include_uncertified: bool = False) -> list[dict[str, object]]:
        return self._edges(EDGE_IMPORTS, "source_entity_id", entity_id, include_uncertified=include_uncertified)

    def importers_of(self, entity_id: str, *, include_uncertified: bool = False) -> list[dict[str, object]]:
        return self._edges(EDGE_IMPORTS, "target_entity_id", entity_id, include_uncertified=include_uncertified)

    def refs_to(self, entity_id: str, *, include_uncertified: bool = False) -> list[dict[str, object]]:
        return self._edges(EDGE_REFS, "target_entity_id", entity_id, include_uncertified=include_uncertified)

    def as_test(self, entity_id: str, *, include_uncertified: bool = False) -> dict[str, object]:
        rows = self._edges(
            EDGE_AS_TEST,
            "source_entity_id",
            entity_id,
            include_uncertified=include_uncertified,
        )
        if len(rows) == 1:
            return {"status": "RESOLVED_UNIQUE", "edge": rows[0]}
        if len(rows) > 1:
            return {"status": "REJECTED", "reason": "AMBIGUOUS_TEST_ROLE", "edges": rows}
        return {"status": "REJECTED", "reason": "NOT_CERTIFIED_AS_TEST"}

    def uses_fixture(self, entity_id: str, *, include_uncertified: bool = False) -> list[dict[str, object]]:
        return self._edges(
            EDGE_USES_FIXTURE,
            "source_entity_id",
            entity_id,
            include_uncertified=include_uncertified,
        )


def _validate_build_inputs(reserve_path: Path, readiness_path: Path) -> tuple[dict[str, object], dict[str, object]]:
    reserve = json.loads(reserve_path.read_text(encoding="utf-8"))
    readiness = json.loads(readiness_path.read_text(encoding="utf-8"))
    if readiness.get("status") != READY_STATUS:
        raise ValueError("source readiness has not authorized semantic index construction")
    if readiness.get("authorization") != "semantic_index_build_only_no_gold_scoring_no_training":
        raise ValueError("unexpected source-readiness authorization")
    if readiness.get("reserve_manifest_sha256") != sha256_file(reserve_path):
        raise ValueError("reserve manifest hash does not match source readiness lock")
    if reserve.get("gold_blind") is not True:
        raise ValueError("reserve manifest is not explicitly gold blind")
    samples = reserve.get("samples")
    if not isinstance(samples, list) or len(samples) != int(readiness.get("verified_snapshot_count", -1)):
        raise ValueError("reserve/readiness snapshot count mismatch")
    return reserve, readiness


def build_corpus(
    *,
    reserve_path: Path,
    readiness_path: Path,
    asset_root: Path,
    output_dir: Path,
    report_path: Path,
) -> dict[str, object]:
    reserve, readiness = _validate_build_inputs(reserve_path, readiness_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    entity_writer = JsonlWriter(output_dir / "entities.jsonl")
    scope_writer = JsonlWriter(output_dir / "scopes.jsonl")
    edge_writer = JsonlWriter(output_dir / "edges.jsonl")
    site_writer = JsonlWriter(output_dir / "resolution_sites.jsonl")
    witness_writer = JsonlWriter(output_dir / "resolution_witnesses.jsonl")
    rejection_writer = JsonlWriter(output_dir / "rejections.jsonl")
    ledger = RejectionLedger()
    snapshot_reports: list[dict[str, object]] = []
    total_git_blob_reads = 0
    total_git_blob_bytes = 0

    samples = sorted(reserve["samples"], key=lambda item: int(item["reserve_index"]))
    for sample in samples:
        repo = str(sample["repo"])
        commit = str(sample["base_commit"])
        repo_dir = _repo_store(asset_root, repo)
        if not repo_dir.is_dir():
            raise FileNotFoundError(f"missing bare Git store: {repo_dir}")
        _git(repo_dir, "cat-file", "-e", f"{commit}^{{commit}}")
        entries = _python_tree_entries(repo_dir, commit)
        oid_paths: dict[str, list[dict[str, object]]] = defaultdict(list)
        for entry in entries:
            oid_paths[str(entry["oid"])].append(entry)
        builder = SnapshotBuilder(
            repo=repo,
            commit=commit,
            paths=[str(item["path"]) for item in entries],
            emit_entity=entity_writer.write,
            emit_scope=scope_writer.write,
            emit_edge=edge_writer.write,
            emit_site=site_writer.write,
            emit_witness=witness_writer.write,
            ledger=ledger,
        )
        for oid, data in _read_blobs(repo_dir, sorted(oid_paths)):
            total_git_blob_reads += 1
            total_git_blob_bytes += len(data)
            for entry in oid_paths[oid]:
                if len(data) != int(entry["bytes"]):
                    raise RuntimeError(f"Git blob size mismatch: {repo}@{commit}:{entry['path']}")
                builder.add_source(str(entry["path"]), oid, data)
        snapshot = builder.finalize()
        snapshot["sample_id"] = sample["sample_id"]
        snapshot["task_type"] = sample["task_type"]
        snapshot["query_paths_indexed"] = sorted(sample.get("query_paths", []))
        snapshot_reports.append(snapshot)

    for row in ledger.example_rows():
        rejection_writer.write(row)
    entity_artifact = entity_writer.close()
    scope_artifact = scope_writer.close()
    edge_artifact = edge_writer.close()
    site_artifact = site_writer.close()
    witness_artifact = witness_writer.close()
    rejection_artifact = rejection_writer.close()
    artifacts = {
        "entities": entity_artifact,
        "scopes": scope_artifact,
        "edges": edge_artifact,
        "resolution_sites": site_artifact,
        "resolution_witnesses": witness_artifact,
        "rejections": rejection_artifact,
    }
    manifest: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "status": INDEX_STATUS,
        "authorization": "semantic_index_query_only_validation_only_no_program_execution_no_scoring_no_training",
        "gold_blind": True,
        "gold_inputs_read": [],
        "source_policy": "complete_python_git_blobs_only",
        "fallback_policy": "reject_ambiguity_and_dynamic_dispatch_no_name_cooccurrence",
        "reserve_manifest_sha256": sha256_file(reserve_path),
        "readiness_report_sha256": sha256_file(readiness_path),
        "source_blob_manifest_sha256": readiness.get("blob_manifest_sha256"),
        "tool_sha256": sha256_file(Path(__file__)),
        "snapshot_count": len(snapshot_reports),
        "python_file_rows": sum(int(item["python_file_count"]) for item in snapshot_reports),
        "python_source_bytes_indexed": sum(int(item["python_bytes_read"]) for item in snapshot_reports),
        "unique_git_blob_reads_per_snapshot_sum": total_git_blob_reads,
        "unique_git_blob_bytes_read_per_snapshot_sum": total_git_blob_bytes,
        "artifacts": artifacts,
        "relation_counts": dict(sorted(edge_writer.relation_counts.items())),
        "edge_resolution_status_counts": dict(sorted(edge_writer.resolution_status_counts.items())),
        "rejection_counts": ledger.count_record(),
        "rejection_examples_per_operation_reason_cap": ledger.examples_per_key,
        "rejection_examples_are_bounded": True,
        "resolution_site_storage": {
            "all_canonical_sites_persisted": True,
            "canonical_key": [
                "repo",
                "commit",
                "operation",
                "source_entity_id",
                "scope_id",
                "expression",
                "resolution_status",
                "candidate_entity_ids (complete, sorted)",
                "reason",
                "proof",
            ],
            "candidate_truncation": "none",
            "occurrence_storage": "first_witness_plus_last_witness_when_distinct_plus_exact_occurrence_count",
            "canonical_row_upper_bound": "raw_resolution_site_occurrences",
            "raw_resolution_site_occurrences": sum(
                int(item["raw_resolution_site_occurrences"]) for item in snapshot_reports
            ),
            "canonical_resolution_site_rows": sum(
                int(item["canonical_resolution_site_rows"]) for item in snapshot_reports
            ),
        },
        "relation_edge_storage": {
            "candidate_truncation": "none",
            "one_row_per_source_target_expression_status_and_proof": True,
            "canonical_row_upper_bound": "raw_relation_edge_occurrences",
            "raw_relation_edge_occurrences": sum(
                int(item["raw_relation_edge_occurrences"]) for item in snapshot_reports
            ),
            "canonical_relation_edge_rows": sum(
                int(item["canonical_relation_edge_rows"]) for item in snapshot_reports
            ),
        },
        "primitive_edge_policy": "one_direct_edge_per_step_no_hidden_macro_or_extra_index",
        "refined_query_default": "CERTIFIED_edges_only",
        "coarse_query_option": "include_uncertified_exposes_same_AMBIGUOUS_or_DYNAMIC_candidates",
        "fanout_policy": "not_applied_by_index_must_be_capped_before_type_filtering_by_caller",
        "depth_accounting": {
            "DEFS_AT": 0,
            "RESOLVE_UNIQUE": 0,
            "AS_TEST": 0,
            "each_directional_relation_primitive": 1,
        },
        "snapshots": snapshot_reports,
        "implemented_primitives": [
            "DEFS_AT",
            "RESOLVE_UNIQUE",
            "CALLEES_OF",
            "CALLERS_OF",
            "IMPORTS_OF",
            "IMPORTERS_OF",
            "REFS_TO",
            "AS_TEST",
            "USES_FIXTURE",
        ],
        "certified_resolution_strategies": [
            "lexical_unique_definition_or_import",
            "explicit_module_alias_attribute",
            "explicit_from_import",
            "same_class_self_or_classmethod_cls_member",
            "lexical_or_imported_class_static_member",
            "pytest_test_name_and_path_convention",
            "explicit_pytest_fixture_decorator_and_nearest_visible_fixture",
        ],
        "known_non_capabilities": [
            "runtime_dispatch_or_monkeypatching",
            "object_type_inference_for_arbitrary_attributes",
            "inheritance_or_descriptor_dispatch",
            "star_import_namespace_expansion",
            "assignment_alias_dataflow",
            "namespace_packages_without_init_evidence",
            "pytest_plugin_or_builtin_fixture_discovery",
            "semantic_retrieval_scoring_or_gold_evaluation",
        ],
    }
    manifest_path = output_dir / "manifest.json"
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    manifest_path.write_text(manifest_text, encoding="utf-8", newline="\n")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(manifest_text, encoding="utf-8", newline="\n")
    return manifest


def _query(layer: PrimitiveLayer, args: argparse.Namespace) -> object:
    primitive = args.primitive
    if primitive == "DEFS_AT":
        if not args.path or not args.repo or not args.commit:
            raise ValueError("DEFS_AT requires --path, --repo, and --commit snapshot partition")
        return layer.defs_at(
            path=args.path,
            lineno=args.lineno,
            name=args.name,
            repo=args.repo,
            commit=args.commit,
        )
    if primitive == "RESOLVE_UNIQUE":
        if (
            not args.scope_id
            or args.expression is None
            or args.lineno is None
            or args.col_offset is None
            or not args.repo
            or not args.commit
        ):
            raise ValueError(
                "RESOLVE_UNIQUE requires --scope-id, --expression, --lineno, "
                "--col-offset, --repo, and --commit"
            )
        return layer.resolve_unique(
            scope_id=args.scope_id,
            expression=args.expression,
            lineno=args.lineno,
            col_offset=args.col_offset,
            repo=args.repo,
            commit=args.commit,
        )
    if not args.entity_id:
        raise ValueError(f"{primitive} requires --entity-id")
    functions = {
        "CALLEES_OF": layer.callees_of,
        "CALLERS_OF": layer.callers_of,
        "IMPORTS_OF": layer.imports_of,
        "IMPORTERS_OF": layer.importers_of,
        "REFS_TO": layer.refs_to,
        "AS_TEST": layer.as_test,
        "USES_FIXTURE": layer.uses_fixture,
    }
    return functions[primitive](args.entity_id, include_uncertified=args.include_uncertified)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    build = subparsers.add_parser("build")
    build.add_argument("--reserve", type=Path, required=True)
    build.add_argument("--readiness", type=Path, required=True)
    build.add_argument("--asset-root", type=Path, required=True)
    build.add_argument("--output-dir", type=Path, required=True)
    build.add_argument("--report", type=Path, required=True)

    query = subparsers.add_parser("query")
    query.add_argument("--index-dir", type=Path, required=True)
    query.add_argument(
        "--primitive",
        required=True,
        choices=[
            "DEFS_AT",
            "RESOLVE_UNIQUE",
            "CALLEES_OF",
            "CALLERS_OF",
            "IMPORTS_OF",
            "IMPORTERS_OF",
            "REFS_TO",
            "AS_TEST",
            "USES_FIXTURE",
        ],
    )
    query.add_argument("--entity-id")
    query.add_argument("--scope-id")
    query.add_argument("--expression")
    query.add_argument("--path")
    query.add_argument("--lineno", type=int)
    query.add_argument("--col-offset", type=int)
    query.add_argument("--name")
    query.add_argument("--repo")
    query.add_argument("--commit")
    query.add_argument(
        "--include-uncertified",
        action="store_true",
        help="Expose the same AMBIGUOUS/DYNAMIC candidate edges to a coarse baseline.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command == "build":
        manifest = build_corpus(
            reserve_path=args.reserve,
            readiness_path=args.readiness,
            asset_root=args.asset_root,
            output_dir=args.output_dir,
            report_path=args.report,
        )
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
    else:
        layer = PrimitiveLayer.from_directory(args.index_dir)
        print(json.dumps(_query(layer, args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
