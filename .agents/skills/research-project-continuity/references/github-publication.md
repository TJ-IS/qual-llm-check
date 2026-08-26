# GitHub publication protocol

The repository owner performs the final push. Preparation must not rewrite or discard user history.

## Preserve

- `.agents/skills/` project skills, including Otero access instructions;
- `docs/research_program/` maps, current state, public requirement registry, curated history, manifest, and checklist;
- canonical Otero full-text corpus and its metadata/results/summary when publication rights allow;
- frozen prompts/configs, decision records, audit summaries, and scripts for accepted/provisional screening runs;
- v11 canonical manuscript ledgers, selected source-comparison records, and current/rejected-predecessor manuscripts with status labels;
- source code, tests, and minimal reproducibility instructions.

## Ignore or select narrowly

- credentials, `.env`, provider configuration, and local machine state;
- virtual environments, caches, build products, logs, and temporary exports;
- `pilot_assets/` or other large externally versioned assets unless redistribution rights and necessity are documented;
- duplicate/obsolete full-text collections when a canonical corpus exists;
- entire audit directories containing repetitive mappings, copied source PDFs/HTML, or rebuildable receipts when a small manifest and representative evidence suffice;
- private raw task transcripts and ignored exact-quote requirement-provenance audits; publish only their normalized control/disposition layer.

## Cross-platform continuation

Prepare the repository so a fresh Codex task can continue from either Windows or macOS without rewriting durable paths or instructions.

- Keep committed paths repository-relative, use forward slashes in manifests and command examples, and preserve exact filename case. A path that resolves only because Windows ignored case is a blocker. Reject case-fold or Unicode-normalization filename collisions before staging because a case-insensitive macOS checkout may collapse them.
- Keep text artifacts UTF-8 and Git-normalized to LF. Python files with shebangs must not acquire CRLF, which breaks direct execution on macOS.
- Repository Python helpers require Python 3.10 or newer. Use `python3` on macOS/Linux; use `python` or the workspace-bundled interpreter on Windows. Never commit a user-specific interpreter path.
- Prefer standard-library Python and `pathlib` for shared helpers. When a workflow genuinely needs a platform shell, provide equivalent Windows and POSIX invocations or route the operation through a cross-platform script.
- A static Windows-side audit can establish relative paths, exact case, encodings, line endings, and interpreter-independent syntax. It cannot claim that macOS execution passed. Close the handoff only after the clean clone runs the documented smoke tests on macOS, or retain `macos_runtime=unverified` as a named condition.

## Technical preflight

1. Inspect `git status`, current diffs, ignored files, and tracked secret-like names.
2. Confirm required CSV/JSONL evidence is not accidentally hidden by broad ignore rules.
3. Identify files above 50 MiB and 100 MiB; GitHub blocks ordinary Git objects above 100 MiB.
4. Estimate the selected repository payload and initial-push pack. GitHub enforces a 2 GiB maximum for a single push and recommends keeping repositories well below 10 GiB on disk.
5. Check wide directories and path length. GitHub recommends fewer than about 3,000 entries in one directory for performance; a wide canonical corpus may warrant a compatibility-preserving shard/archive plan.
6. Use Git LFS only after deciding that large binary/object storage and quota trade-offs are appropriate. Do not add LFS as decoration for many small compressible text files.
7. Add a license only when the owner chooses terms and confirms third-party corpus redistribution rights. Do not invent a license.
8. Add citation metadata only after author/title/identifier fields are confirmed.
9. Inspect `.gitattributes`, case-exact manifest paths, case/Unicode-normalization filename collisions, path-component byte limits, Python version requirements, and platform-neutral command examples.
10. Stage by manifest, inspect the staged diff and large-file list, then let the owner push.

Official references:

- GitHub repository limits: <https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits>
- Large-file guidance: <https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github>
- Git LFS billing/quotas: <https://docs.github.com/en/billing/concepts/product-billing/git-lfs>

## Corpus-specific rule

`database_fulltext_all/` is the current canonical Otero corpus. `database_fulltext_construct/` is an older/overlapping construct-query collection and should not be published as a second canonical corpus. Preserve the canonical corpus's identity and compatibility; if sharding or packaging is needed, provide a manifest and migration script before changing paths.
