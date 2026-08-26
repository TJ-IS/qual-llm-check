from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote

from semantic_ast_index import PrimitiveLayer, build_from_source_mapping, make_entity_id, parse_entity_id


SOURCES = {
    "src/pkg/__init__.py": "",
    "src/pkg/a.py": """
from .b import helper as imported_helper

def local():
    return 1

def caller():
    return imported_helper() + local()

class C:
    def m(self):
        return self.n()

    def n(self):
        return local()

def dynamic(obj):
    return obj.run()

from .b import helper as choice
from .c import helper as choice

def ambiguous():
    return choice()

def no_fallback():
    return missing_helper()

def repeated():
    return local() + local() + local()

def lambda_owner():
    first = lambda: local()
    second = lambda: local()
    return first, second
""",
    "src/pkg/b.py": """
def helper():
    return 2
""",
    "src/pkg/c.py": """
def helper():
    return 3

def missing_helper():
    return 4
""",
    "tests/conftest.py": """
import pytest

@pytest.fixture
def client():
    return object()
""",
    "tests/test_use.py": """
from pkg.a import caller

def test_flow(client):
    return caller()
""",
}


class SemanticAstIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = build_from_source_mapping(
            repo="org/repo",
            commit="a" * 40,
            sources=SOURCES,
        )
        cls.layer = PrimitiveLayer(
            cls.result["entities"],
            cls.result["scopes"],
            cls.result["edges"],
            cls.result["resolution_sites"],
            cls.result["resolution_witnesses"],
        )

    @classmethod
    def entity(cls, path: str, qualname: str) -> dict:
        matches = [
            item
            for item in cls.result["entities"]
            if item["path"] == path and item["qualname"] == qualname
        ]
        if len(matches) != 1:
            raise AssertionError((path, qualname, matches))
        return matches[0]

    @staticmethod
    def call_position(result: dict, entity_id: str, expression: str) -> tuple[int, int]:
        rows = [
            item
            for item in result["resolution_witnesses"]
            if item["expression"] == expression
            and any(
                site["site_id"] == item["site_id"]
                and site["source_entity_id"] == entity_id
                and site["operation"] == "CALLEES_OF"
                for site in result["resolution_sites"]
            )
        ]
        if not rows:
            raise AssertionError((entity_id, expression))
        return int(rows[0]["lineno"]), int(rows[0]["col_offset"])

    @staticmethod
    def fixture_entity(result: dict, path: str, qualname: str) -> dict:
        rows = [
            item
            for item in result["entities"]
            if item["path"] == path and item["qualname"] == qualname
        ]
        if len(rows) != 1:
            raise AssertionError((path, qualname, rows))
        return rows[0]

    @staticmethod
    def fixture_sites(result: dict, source_entity_id: str, operation: str, expression: str | None = None) -> list[dict]:
        return [
            item
            for item in result["resolution_sites"]
            if item["source_entity_id"] == source_entity_id
            and item["operation"] == operation
            and (expression is None or item["witness"]["expression"] == expression)
        ]

    def test_entity_id_is_reversible_and_contains_all_required_fields(self) -> None:
        entity = self.entity("src/pkg/a.py", "C.m")
        entity_id = entity["entity_id"]
        self.assertTrue(entity_id.startswith("pyent:v1|"))
        decoded = {}
        for part in entity_id.split("|")[1:]:
            key, value = part.split("=", 1)
            decoded[key] = unquote(value)
        for field in (
            "repo",
            "commit",
            "path",
            "qualname",
            "lineno",
            "end_lineno",
            "kind",
            "blob_oid",
        ):
            self.assertEqual(decoded[field], str(entity[field]))
        self.assertEqual(parse_entity_id(entity_id), {field: entity[field] for field in decoded})

    def test_entity_id_round_trip_survives_delimiters(self) -> None:
        identity = {
            "repo": "org/repo|variant=1%",
            "commit": "c" * 40,
            "path": "src/a|b=c%20.py",
            "qualname": "Outer.<locals>.f|g=h%",
            "lineno": 7,
            "end_lineno": 11,
            "kind": "function|synthetic=0",
            "blob_oid": "d" * 40,
        }
        encoded = make_entity_id(identity)
        self.assertEqual(parse_entity_id(encoded), identity)

    def test_narrow_core_certifies_only_same_module_name_bindings(self) -> None:
        caller = self.entity("src/pkg/a.py", "caller")
        helper = self.entity("src/pkg/b.py", "helper")
        local = self.entity("src/pkg/a.py", "local")
        method_m = self.entity("src/pkg/a.py", "C.m")
        method_n = self.entity("src/pkg/a.py", "C.n")

        caller_targets = {edge["target_entity_id"] for edge in self.layer.callees_of(caller["entity_id"])}
        self.assertEqual(caller_targets, {local["entity_id"]})
        coarse_caller_targets = {
            edge["target_entity_id"]
            for edge in self.layer.callees_of(caller["entity_id"], include_uncertified=True)
        }
        self.assertEqual(coarse_caller_targets, {helper["entity_id"], local["entity_id"]})
        method_targets = {edge["target_entity_id"] for edge in self.layer.callees_of(method_m["entity_id"])}
        self.assertEqual(method_targets, set())
        nominal_candidates = self.layer.callees_of(method_m["entity_id"], include_uncertified=True)
        self.assertEqual({edge["target_entity_id"] for edge in nominal_candidates}, {method_n["entity_id"]})
        self.assertEqual({edge["resolution_status"] for edge in nominal_candidates}, {"DYNAMIC"})
        for edge in self.layer.callees_of(caller["entity_id"]):
            self.assertEqual(edge["resolution_status"], "CERTIFIED")
            self.assertIn("resolver", edge["witness"])

    def test_ambiguous_and_dynamic_sites_are_not_silently_dropped(self) -> None:
        ambiguous = self.entity("src/pkg/a.py", "ambiguous")
        helper_b = self.entity("src/pkg/b.py", "helper")
        helper_c = self.entity("src/pkg/c.py", "helper")
        refined = self.layer.callees_of(ambiguous["entity_id"])
        coarse = self.layer.callees_of(ambiguous["entity_id"], include_uncertified=True)
        self.assertEqual(refined, [])
        self.assertEqual({edge["target_entity_id"] for edge in coarse}, {helper_b["entity_id"], helper_c["entity_id"]})
        self.assertEqual({edge["resolution_status"] for edge in coarse}, {"AMBIGUOUS"})

        scope_id = ambiguous["scope_id"]
        line, col = self.call_position(self.result, ambiguous["entity_id"], "choice")
        resolution = self.layer.resolve_unique(
            scope_id=scope_id,
            expression="choice",
            lineno=line,
            col_offset=col,
        )
        self.assertEqual(resolution["status"], "REJECTED")
        self.assertEqual(resolution["reason"], "AMBIGUOUS_IMPORT_BINDING")

        dynamic = self.entity("src/pkg/a.py", "dynamic")
        line, col = self.call_position(self.result, dynamic["entity_id"], "obj.run")
        dynamic_result = self.layer.resolve_unique(
            scope_id=dynamic["scope_id"],
            expression="obj.run",
            lineno=line,
            col_offset=col,
        )
        self.assertEqual(dynamic_result["status"], "REJECTED")
        self.assertEqual(dynamic_result["reason"], "DYNAMIC_OR_REBOUND_ATTRIBUTE_ROOT")
        dynamic_sites = [
            site
            for site in self.result["resolution_sites"]
            if site["source_entity_id"] == dynamic["entity_id"]
            and site["operation"] == "CALLEES_OF"
        ]
        self.assertEqual(len(dynamic_sites), 1)
        self.assertEqual(dynamic_sites[0]["resolution_status"], "DYNAMIC")

    def test_no_name_cooccurrence_fallback(self) -> None:
        no_fallback = self.entity("src/pkg/a.py", "no_fallback")
        misleading = self.entity("src/pkg/c.py", "missing_helper")
        all_candidates = self.layer.callees_of(no_fallback["entity_id"], include_uncertified=True)
        self.assertEqual(all_candidates, [])
        sites = [
            site
            for site in self.result["resolution_sites"]
            if site["source_entity_id"] == no_fallback["entity_id"]
            and site["operation"] == "CALLEES_OF"
        ]
        self.assertEqual(len(sites), 1)
        self.assertEqual(sites[0]["candidate_entity_ids"], [])
        self.assertNotIn(misleading["entity_id"], sites[0]["candidate_entity_ids"])

    def test_canonical_site_dedup_keeps_exact_count_and_complete_candidates(self) -> None:
        repeated = self.entity("src/pkg/a.py", "repeated")
        local = self.entity("src/pkg/a.py", "local")
        call_sites = [
            site
            for site in self.result["resolution_sites"]
            if site["source_entity_id"] == repeated["entity_id"]
            and site["operation"] == "CALLEES_OF"
            and site["witness"]["expression"] == "local"
        ]
        self.assertEqual(len(call_sites), 1)
        self.assertEqual(call_sites[0]["occurrence_count"], 3)
        self.assertEqual(call_sites[0]["candidate_entity_ids"], [local["entity_id"]])
        witness_rows = self.layer.witnesses_for(call_sites[0]["site_id"])
        self.assertEqual(len(witness_rows), 3)
        self.assertEqual([row["witness_ordinal"] for row in witness_rows], [1, 2, 3])
        self.assertEqual(
            [(int(row["lineno"]), int(row["col_offset"])) for row in witness_rows],
            [(30, 11), (30, 21), (30, 31)],
        )
        call_edges = [
            edge
            for edge in self.layer.callees_of(repeated["entity_id"])
            if edge["target_entity_id"] == local["entity_id"]
        ]
        self.assertEqual(len(call_edges), 1)
        self.assertEqual(call_edges[0]["occurrence_count"], 3)
        self.assertEqual(call_edges[0]["resolution_site_id"], call_sites[0]["site_id"])
        self.assertEqual(
            sum(int(site["occurrence_count"]) for site in self.result["resolution_sites"]),
            self.result["summary"]["raw_resolution_site_occurrences"],
        )
        self.assertEqual(
            len(self.result["resolution_witnesses"]),
            self.result["summary"]["raw_resolution_site_occurrences"],
        )
        self.assertEqual(
            sum(int(edge["occurrence_count"]) for edge in self.result["edges"]),
            self.result["summary"]["raw_relation_edge_occurrences"],
        )
        self.assertLessEqual(
            self.result["summary"]["canonical_resolution_site_rows"],
            self.result["summary"]["raw_resolution_site_occurrences"],
        )

    def test_dynamic_site_with_no_candidates_is_queryable_with_its_witness(self) -> None:
        dynamic = self.entity("src/pkg/a.py", "dynamic")
        sites = self.layer.resolution_sites_of(
            repo="org/repo",
            commit="a" * 40,
            source_entity_id=dynamic["entity_id"],
            operation="CALLEES_OF",
            resolution_status="DYNAMIC",
        )
        sites = [site for site in sites if site["witness"]["expression"] == "obj.run"]
        self.assertEqual(len(sites), 1)
        self.assertEqual(sites[0]["candidate_entity_ids"], [])
        witnesses = self.layer.witnesses_for(sites[0]["site_id"])
        self.assertEqual(len(witnesses), 1)
        self.assertEqual(witnesses[0]["expression"], "obj.run")

    def test_identical_lambda_expressions_keep_distinct_scope_sites_and_edges(self) -> None:
        owner = self.entity("src/pkg/a.py", "lambda_owner")
        local = self.entity("src/pkg/a.py", "local")
        sites = self.fixture_sites(self.result, owner["entity_id"], "CALLEES_OF", "local")
        self.assertEqual(len(sites), 2)
        self.assertEqual(len({site["scope_id"] for site in sites}), 2)
        self.assertEqual({tuple(site["candidate_entity_ids"]) for site in sites}, {(local["entity_id"],)})
        edges = [
            edge
            for edge in self.layer.callees_of(owner["entity_id"], include_uncertified=True)
            if edge["target_entity_id"] == local["entity_id"]
        ]
        self.assertEqual(len(edges), 2)
        self.assertEqual({edge["resolution_site_id"] for edge in edges}, {site["site_id"] for site in sites})

    def test_staticmethod_decorator_and_conditional_definitions_fail_closed(self) -> None:
        result = build_from_source_mapping(
            repo="org/counterexamples",
            commit="3" * 40,
            sources={
                "mod.py": """
def replace(fn):
    return fn

@replace
def decorated_target():
    return 1

def decorated_caller():
    return decorated_target()

if False:
    def conditional_target():
        return 2

def conditional_caller():
    return conditional_target()

class C:
    @staticmethod
    def m(self):
        return self.n()

    def n(self):
        return 3
""",
            },
        )
        cases = (
            ("decorated_caller", "decorated_target", "DECORATED_BINDING_MAY_REPLACE"),
            ("conditional_caller", "conditional_target", "CONDITIONAL_BINDING_NOT_DOMINATING"),
            ("C.m", "self.n", "STATICMETHOD_RECEIVER_NOT_INSTANCE"),
        )
        for qualname, expression, reason in cases:
            with self.subTest(qualname=qualname):
                source = self.fixture_entity(result, "mod.py", qualname)
                sites = self.fixture_sites(result, source["entity_id"], "CALLEES_OF", expression)
                self.assertEqual(len(sites), 1)
                self.assertEqual(sites[0]["resolution_status"], "DYNAMIC")
                self.assertEqual(sites[0]["reason"], reason)
                certified = [
                    edge
                    for edge in result["edges"]
                    if edge["edge_type"] == "CALLS"
                    and edge["source_entity_id"] == source["entity_id"]
                    and edge["resolution_status"] == "CERTIFIED"
                ]
                self.assertEqual(certified, [])

    def test_type_alias_rebinding_and_python_execution_order_fail_closed(self) -> None:
        result = build_from_source_mapping(
            repo="org/order",
            commit="4" * 40,
            sources={
                "mod.py": """
def existing():
    return 0

def target(x=target()):
    return x

def annotated(x: annotated()):
    return x

class Base(Base):
    pass

class Body:
    value = Body

def caller():
    return late()
caller()
def late():
    return 1

def A():
    return 2
type A = int
def alias_caller():
    return A()
""",
            },
        )
        cases = (
            ("<module>", "target", "CALLEES_OF", "BINDING_NOT_DOMINATING_SITE"),
            ("<module>", "annotated", "CALLEES_OF", "BINDING_NOT_DOMINATING_SITE"),
            ("<module>", "Base", "REFS_TO", "BINDING_NOT_DOMINATING_SITE"),
            ("Body", "Body", "REFS_TO", "SOURCE_SCOPE_OUTSIDE_CONSERVATIVE_CERTIFICATE"),
            ("caller", "late", "CALLEES_OF", "CROSS_SCOPE_BINDING_NOT_AVAILABLE_AT_FUNCTION_DEFINITION"),
            ("alias_caller", "A", "CALLEES_OF", "DYNAMIC_OR_REBOUND_LOCAL"),
        )
        for qualname, expression, operation, reason in cases:
            with self.subTest(qualname=qualname):
                source = self.fixture_entity(result, "mod.py", qualname)
                matching = self.fixture_sites(result, source["entity_id"], operation, expression)
                self.assertTrue(matching)
                self.assertTrue(all(site["resolution_status"] == "DYNAMIC" for site in matching))
                self.assertIn(reason, {site["reason"] for site in matching})

    def test_nested_and_rebound_pytest_roles_are_not_certified(self) -> None:
        result = build_from_source_mapping(
            repo="org/pytest-counterexamples",
            commit="5" * 40,
            sources={
                "tests/test_nested.py": """
def factory():
    import pytest
    @pytest.fixture
    def client():
        return object()
    def test_hidden(client):
        return client
    return test_hidden

def test_visible(client):
    return client
""",
                "tests/test_rebound.py": """
import pytest
pytest = object()

@pytest.fixture
def client():
    return object()

def test_rebound_visible(client):
    return client
""",
            },
        )
        nested_fixture = self.fixture_entity(result, "tests/test_nested.py", "factory.<locals>.client")
        nested_test = self.fixture_entity(result, "tests/test_nested.py", "factory.<locals>.test_hidden")
        rebound_fixture = self.fixture_entity(result, "tests/test_rebound.py", "client")
        for entity, operation, reason in (
            (nested_fixture, "AS_FIXTURE", "PYTEST_NESTED_NOT_COLLECTIBLE"),
            (nested_test, "AS_TEST", "PYTEST_NESTED_NOT_COLLECTIBLE"),
            (rebound_fixture, "AS_FIXTURE", "PYTEST_DECORATOR_BINDING_REBOUND"),
        ):
            sites = self.fixture_sites(result, entity["entity_id"], operation)
            self.assertEqual(len(sites), 1)
            self.assertEqual(sites[0]["resolution_status"], "DYNAMIC")
            self.assertEqual(sites[0]["reason"], reason)
        visible_ids = {
            self.fixture_entity(result, "tests/test_nested.py", "test_visible")["entity_id"],
            self.fixture_entity(result, "tests/test_rebound.py", "test_rebound_visible")["entity_id"],
        }
        self.assertFalse(
            any(
                edge["edge_type"] == "USES_FIXTURE" and edge["source_entity_id"] in visible_ids
                for edge in result["edges"]
            )
        )

    def test_import_certificates_require_module_scope_and_stable_target_export(self) -> None:
        result = build_from_source_mapping(
            repo="org/import-counterexamples",
            commit="6" * 40,
            sources={
                "src/pkg/__init__.py": "",
                "src/pkg/stable.py": """
def helper():
    return 1
""",
                "src/pkg/conditional.py": """
if False:
    def helper():
        return 2
""",
                "src/pkg/rebound.py": """
def helper():
    return 3
helper = object()
""",
                "src/pkg/decorated.py": """
def replace(fn):
    return fn
@replace
def helper():
    return 4
""",
                "src/pkg/use.py": """
from .conditional import helper as conditional_helper
from .rebound import helper as rebound_helper
from .decorated import helper as decorated_helper

def outer():
    from .stable import helper as local_helper
    return local_helper()

class Holder:
    from .stable import helper as class_helper
""",
            },
        )
        module_use = self.fixture_entity(result, "src/pkg/use.py", "<module>")
        outer = self.fixture_entity(result, "src/pkg/use.py", "outer")
        holder = self.fixture_entity(result, "src/pkg/use.py", "Holder")
        stable = self.fixture_entity(result, "src/pkg/stable.py", "helper")
        cases = (
            (outer, "IMPORT_SCOPE_OUTSIDE_CONSERVATIVE_CERTIFICATE", stable["entity_id"]),
            (holder, "IMPORT_SCOPE_OUTSIDE_CONSERVATIVE_CERTIFICATE", stable["entity_id"]),
            (module_use, "CONDITIONAL_BINDING_NOT_DOMINATING", self.fixture_entity(result, "src/pkg/conditional.py", "helper")["entity_id"]),
            (module_use, "TARGET_EXPORT_DYNAMIC_OR_REBOUND", self.fixture_entity(result, "src/pkg/rebound.py", "helper")["entity_id"]),
            (module_use, "DECORATED_BINDING_MAY_REPLACE", self.fixture_entity(result, "src/pkg/decorated.py", "helper")["entity_id"]),
        )
        for source, reason, target_id in cases:
            with self.subTest(source=source["qualname"], reason=reason):
                certified = [
                    edge
                    for edge in result["edges"]
                    if edge["edge_type"] == "IMPORTS"
                    and edge["source_entity_id"] == source["entity_id"]
                    and edge["target_entity_id"] == target_id
                    and edge["resolution_status"] == "CERTIFIED"
                ]
                self.assertEqual(certified, [])
                dynamic = [
                    edge
                    for edge in result["edges"]
                    if edge["edge_type"] == "IMPORTS"
                    and edge["source_entity_id"] == source["entity_id"]
                    and edge["target_entity_id"] == target_id
                    and edge["resolution_status"] == "DYNAMIC"
                ]
                self.assertTrue(dynamic)
                site = next(
                    item
                    for item in result["resolution_sites"]
                    if item["site_id"] == dynamic[0]["resolution_site_id"]
                )
                self.assertEqual(site["reason"], reason)
                self.assertEqual(site["candidate_entity_ids"], [target_id])

    def test_cross_module_symbol_imports_remain_candidates_after_alias_mutation(self) -> None:
        result = build_from_source_mapping(
            repo="org/cross-module-mutation",
            commit="8" * 40,
            sources={
                "src/pkg/__init__.py": "",
                "src/pkg/b.py": """
def helper():
    return 1
""",
                "src/pkg/c.py": """
def other():
    return 2
""",
                "src/pkg/use.py": """
import pkg.b as b
from pkg.c import other
b.helper = other
from pkg.b import helper as h

def caller():
    return h()
""",
            },
        )
        module_use = self.fixture_entity(result, "src/pkg/use.py", "<module>")
        caller = self.fixture_entity(result, "src/pkg/use.py", "caller")
        helper = self.fixture_entity(result, "src/pkg/b.py", "helper")
        module_b = self.fixture_entity(result, "src/pkg/b.py", "<module>")
        certified_imports = [
            edge
            for edge in result["edges"]
            if edge["edge_type"] == "IMPORTS"
            and edge["source_entity_id"] == module_use["entity_id"]
            and edge["resolution_status"] == "CERTIFIED"
        ]
        self.assertEqual([edge["target_entity_id"] for edge in certified_imports], [module_b["entity_id"]])
        self.assertEqual(certified_imports[0]["witness"]["resolver"], "SOURCE_SYNTAX_MODULE_IMPORT")
        symbol_imports = [
            edge
            for edge in result["edges"]
            if edge["edge_type"] == "IMPORTS"
            and edge["source_entity_id"] == module_use["entity_id"]
            and edge["target_entity_id"] == helper["entity_id"]
        ]
        self.assertEqual(len(symbol_imports), 1)
        self.assertEqual(symbol_imports[0]["resolution_status"], "DYNAMIC")
        call_edges = [
            edge
            for edge in result["edges"]
            if edge["edge_type"] == "CALLS"
            and edge["source_entity_id"] == caller["entity_id"]
            and edge["target_entity_id"] == helper["entity_id"]
        ]
        self.assertEqual(len(call_edges), 1)
        self.assertEqual(call_edges[0]["resolution_status"], "DYNAMIC")
        call_site = next(
            item
            for item in result["resolution_sites"]
            if item["site_id"] == call_edges[0]["resolution_site_id"]
        )
        self.assertEqual(call_site["candidate_entity_ids"], [helper["entity_id"]])

    def test_as_test_requires_a_stable_final_module_export(self) -> None:
        result = build_from_source_mapping(
            repo="org/test-role-counterexamples",
            commit="7" * 40,
            sources={
                "tests/test_assignment.py": """
def test_x():
    pass
test_x = 0
""",
                "tests/test_delete.py": """
def test_x():
    pass
del test_x
""",
                "tests/test_duplicate.py": """
def test_x():
    pass
def test_x():
    pass
""",
                "tests/test_attribute_flag.py": """
def test_x():
    pass
test_x.__test__ = False
""",
            },
        )
        test_entities = [
            item
            for item in result["entities"]
            if item.get("name") == "test_x"
        ]
        self.assertEqual(len(test_entities), 5)
        certified_ids = {
            edge["source_entity_id"]
            for edge in result["edges"]
            if edge["edge_type"] == "AS_TEST" and edge["resolution_status"] == "CERTIFIED"
        }
        self.assertTrue(certified_ids.isdisjoint({item["entity_id"] for item in test_entities}))
        for entity in test_entities:
            sites = self.fixture_sites(result, entity["entity_id"], "AS_TEST")
            self.assertEqual(len(sites), 1)
            self.assertEqual(sites[0]["resolution_status"], "DYNAMIC")
            self.assertIn(
                sites[0]["reason"],
                {"TARGET_EXPORT_DYNAMIC_OR_REBOUND", "TARGET_EXPORT_BINDING_POISONED"},
            )

    def test_directional_import_ref_and_fixture_primitives(self) -> None:
        module_a = self.entity("src/pkg/a.py", "<module>")
        helper = self.entity("src/pkg/b.py", "helper")
        self.assertEqual(self.layer.imports_of(module_a["entity_id"]), [])
        imports = self.layer.imports_of(module_a["entity_id"], include_uncertified=True)
        self.assertIn(helper["entity_id"], {edge["target_entity_id"] for edge in imports})
        importers = self.layer.importers_of(helper["entity_id"], include_uncertified=True)
        self.assertIn(module_a["entity_id"], {edge["source_entity_id"] for edge in importers})
        refs = self.layer.refs_to(helper["entity_id"], include_uncertified=True)
        self.assertTrue(any(edge["witness"]["expression"] == "imported_helper" for edge in refs))

        test = self.entity("tests/test_use.py", "test_flow")
        fixture = self.entity("tests/conftest.py", "client")
        self.assertEqual(self.layer.as_test(test["entity_id"])["status"], "RESOLVED_UNIQUE")
        self.assertEqual(self.layer.uses_fixture(test["entity_id"]), [])
        uses = self.layer.uses_fixture(test["entity_id"], include_uncertified=True)
        self.assertEqual([edge["target_entity_id"] for edge in uses], [fixture["entity_id"]])
        self.assertEqual(uses[0]["resolution_status"], "DYNAMIC")

    def test_defs_at_and_persisted_layer_are_recomputable(self) -> None:
        local = self.entity("src/pkg/a.py", "local")
        matches = self.layer.defs_at(
            path="src/pkg/a.py",
            name="local",
            repo="org/repo",
            commit="a" * 40,
        )
        self.assertEqual([item["entity_id"] for item in matches], [local["entity_id"]])
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for filename, key in (
                ("entities.jsonl", "entities"),
                ("scopes.jsonl", "scopes"),
                ("edges.jsonl", "edges"),
                ("resolution_sites.jsonl", "resolution_sites"),
                ("resolution_witnesses.jsonl", "resolution_witnesses"),
            ):
                with (root / filename).open("w", encoding="utf-8", newline="\n") as handle:
                    for row in self.result[key]:
                        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            persisted = PrimitiveLayer.from_directory(root)
            self.assertEqual(
                {edge["target_entity_id"] for edge in persisted.callees_of(local["entity_id"])},
                set(),
            )
            caller = self.entity("src/pkg/a.py", "caller")
            self.assertEqual(len(persisted.callees_of(caller["entity_id"])), 1)
            dynamic = self.entity("src/pkg/a.py", "dynamic")
            dynamic_sites = persisted.resolution_sites_of(
                repo="org/repo",
                commit="a" * 40,
                source_entity_id=dynamic["entity_id"],
                operation="CALLEES_OF",
                resolution_status="DYNAMIC",
            )
            dynamic_sites = [site for site in dynamic_sites if site["witness"]["expression"] == "obj.run"]
            self.assertEqual(len(dynamic_sites), 1)
            self.assertEqual(dynamic_sites[0]["candidate_entity_ids"], [])
            self.assertEqual(persisted.witnesses_for(dynamic_sites[0]["site_id"])[0]["expression"], "obj.run")

    def test_every_relation_edge_is_atomic_directional_and_witnessed(self) -> None:
        allowed = {"CALLS", "IMPORTS", "REFS_TO", "AS_TEST", "AS_FIXTURE", "USES_FIXTURE"}
        statuses = {"CERTIFIED", "AMBIGUOUS", "DYNAMIC"}
        self.assertTrue(self.result["edges"])
        entities = {item["entity_id"]: item for item in self.result["entities"]}
        scopes = {item["scope_id"]: item for item in self.result["scopes"]}
        sites = {item["site_id"]: item for item in self.result["resolution_sites"]}
        targets_by_site: dict[str, set[str]] = {}
        for edge in self.result["edges"]:
            self.assertIn(edge["edge_type"], allowed)
            self.assertIn(edge["resolution_status"], statuses)
            self.assertIn("source_entity_id", edge)
            self.assertIn("target_entity_id", edge)
            self.assertIn("witness", edge)
            self.assertIn("resolution_site_id", edge)
            site = sites[edge["resolution_site_id"]]
            self.assertEqual(edge["source_entity_id"], site["source_entity_id"])
            self.assertEqual(edge["resolution_status"], site["resolution_status"])
            self.assertIn(edge["target_entity_id"], site["candidate_entity_ids"])
            targets_by_site.setdefault(site["site_id"], set()).add(edge["target_entity_id"])
            source = entities[edge["source_entity_id"]]
            target = entities[edge["target_entity_id"]]
            self.assertEqual((source["repo"], source["commit"]), (target["repo"], target["commit"]))
            if edge["resolution_status"] == "CERTIFIED" and edge["edge_type"] in {"CALLS", "REFS_TO"}:
                source_scope = scopes[source["parent_scope_id"]]
                target_scope = scopes[target["parent_scope_id"]]
                self.assertEqual(source_scope["kind"], "module")
                self.assertEqual(target_scope["kind"], "module")
                self.assertIn(source["kind"], {"function", "async_function"})
                self.assertIn(target["kind"], {"function", "async_function"})
                self.assertEqual(source["module_name"], target["module_name"])
                self.assertEqual(source["definition_certainty"], "unconditional_syntax")
                self.assertEqual(target["definition_certainty"], "unconditional_syntax")
                self.assertFalse(source.get("decorators"))
                self.assertFalse(target.get("decorators"))
                self.assertNotIn(".", edge["witness"]["expression"])
                self.assertEqual(edge["witness"]["resolver"]["strategy"], "lexical_unique_binding")
            if edge["resolution_status"] == "CERTIFIED" and edge["edge_type"] == "IMPORTS":
                self.assertEqual(source["kind"], "module")
                self.assertEqual(target["kind"], "module")
                self.assertEqual(edge["witness"]["resolver"], "SOURCE_SYNTAX_MODULE_IMPORT")
            if edge["resolution_status"] == "CERTIFIED" and edge["edge_type"] in {"AS_FIXTURE", "USES_FIXTURE"}:
                self.fail("pytest fixture collection is outside the conservative certificate core")
        for site in sites.values():
            self.assertEqual(
                targets_by_site.get(site["site_id"], set()),
                set(site["candidate_entity_ids"]),
            )
        self.assertNotIn("TESTS_FOR", allowed)
        self.assertNotIn("IMPORTS_OR_IMPORTERS", allowed)

    def test_persisted_resolver_partitions_same_module_and_qualname_by_commit(self) -> None:
        snapshot_sources = {
            "src/pkg/shared.py": """
def same():
    return VALUE

def caller():
    return same()
""",
        }
        commit_a = "1" * 40
        commit_b = "2" * 40
        result_a = build_from_source_mapping(
            repo="org/shared",
            commit=commit_a,
            sources={"src/pkg/shared.py": snapshot_sources["src/pkg/shared.py"].replace("VALUE", "1")},
        )
        result_b = build_from_source_mapping(
            repo="org/shared",
            commit=commit_b,
            sources={"src/pkg/shared.py": snapshot_sources["src/pkg/shared.py"].replace("VALUE", "2")},
        )
        entities = [*result_a["entities"], *result_b["entities"]]
        scopes = [*result_a["scopes"], *result_b["scopes"]]
        edges = [*result_a["edges"], *result_b["edges"]]
        sites = [*result_a["resolution_sites"], *result_b["resolution_sites"]]
        witnesses = [*result_a["resolution_witnesses"], *result_b["resolution_witnesses"]]
        layer = PrimitiveLayer(entities, scopes, edges, sites, witnesses)

        def entity(commit: str, path: str, qualname: str) -> dict:
            rows = [
                item
                for item in entities
                if item["commit"] == commit and item["path"] == path and item["qualname"] == qualname
            ]
            self.assertEqual(len(rows), 1)
            return rows[0]

        caller_a = entity(commit_a, "src/pkg/shared.py", "caller")
        caller_b = entity(commit_b, "src/pkg/shared.py", "caller")
        target_a = entity(commit_a, "src/pkg/shared.py", "same")
        target_b = entity(commit_b, "src/pkg/shared.py", "same")
        line_a, col_a = self.call_position(result_a, caller_a["entity_id"], "same")
        line_b, col_b = self.call_position(result_b, caller_b["entity_id"], "same")
        resolution_a = layer.resolve_unique(
            scope_id=caller_a["scope_id"], expression="same", lineno=line_a, col_offset=col_a
        )
        resolution_b = layer.resolve_unique(
            scope_id=caller_b["scope_id"], expression="same", lineno=line_b, col_offset=col_b
        )
        self.assertEqual(resolution_a["status"], "RESOLVED_UNIQUE")
        self.assertEqual(resolution_b["status"], "RESOLVED_UNIQUE")
        self.assertEqual(resolution_a["target_entity_id"], target_a["entity_id"])
        self.assertEqual(resolution_b["target_entity_id"], target_b["entity_id"])
        self.assertNotEqual(resolution_a["target_entity_id"], resolution_b["target_entity_id"])
        self.assertEqual(
            layer.defs_at(
                path="src/pkg/shared.py",
                name="same",
                repo="org/shared",
                commit=commit_a,
            )[0]["entity_id"],
            target_a["entity_id"],
        )

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for filename, rows in (
                ("entities.jsonl", entities),
                ("scopes.jsonl", scopes),
                ("edges.jsonl", edges),
                ("resolution_sites.jsonl", sites),
                ("resolution_witnesses.jsonl", witnesses),
            ):
                with (root / filename).open("w", encoding="utf-8", newline="\n") as handle:
                    for row in rows:
                        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            persisted = PrimitiveLayer.from_directory(root)
            persisted_a = persisted.resolve_unique(
                scope_id=caller_a["scope_id"],
                expression="same",
                lineno=line_a,
                col_offset=col_a,
            )
            persisted_b = persisted.resolve_unique(
                scope_id=caller_b["scope_id"],
                expression="same",
                lineno=line_b,
                col_offset=col_b,
            )
            self.assertEqual(persisted_a["target_entity_id"], target_a["entity_id"])
            self.assertEqual(persisted_b["target_entity_id"], target_b["entity_id"])

    def test_incomplete_python_is_rejected_instead_of_partially_indexed(self) -> None:
        with self.assertRaises(RuntimeError):
            build_from_source_mapping(
                repo="org/repo",
                commit="b" * 40,
                sources={"broken.py": "def broken(:\n"},
            )


if __name__ == "__main__":
    unittest.main()
