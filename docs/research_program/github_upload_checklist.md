# GitHub upload checklist

The owner performs the commit and push. Do not start with `git add .`; stage the curated groups below and inspect each one.

## Decisions required from the owner

- [ ] Choose public or private destination.
- [ ] Decide whether journal full texts may be redistributed. If not, publish Otero metadata/results plus a reproducible downloader and keep `database_fulltext_all/` outside the public repository.
- [ ] Choose a license for repository-owned code/skills and determine whether manuscript text uses the same or a separate license. Do not extend that license to third-party articles or databases.
- [ ] Confirm author/title/identifier data before adding `CITATION.cff`.
- [ ] Accept the current compatible flat Otero directory, or schedule a separately tested shard/data-repository migration. The present preparation does not change paths used by scripts.

## Pre-stage checks

- [ ] Review the five pre-existing user modifications listed in the retention manifest.
- [ ] Run `.agents/skills/research-project-continuity/scripts/audit_repository_readiness.py` from the repository root.
- [ ] Confirm `.env` is ignored and inspect the staged tree with a secret scanner. Never print credential values into an audit log.
- [ ] Verify the canonical Otero summary: 13,913 metadata/results, 13,910 downloads, 3 unavailable, 0 failed.
- [ ] Reconcile each screening package's decisions with its `summary.json` and human audit.
- [ ] Confirm v15 manuscripts are described as unaccepted predecessors, not final/accepted papers.
- [ ] Run the selected Markdown/link and screening audit scripts.
- [ ] Confirm public manifests use repository-relative forward-slash paths with exact filename case, and no committed instruction hard-codes a local drive, home directory, or bundled-runtime version.
- [ ] Confirm `.gitattributes` normalizes Markdown, Python, JSON/JSONL, YAML, CSV, and text files to LF.
- [ ] Require zero case-fold/Unicode-normalization filename collisions and zero path components above 255 UTF-8 bytes in the selected publication tree; default macOS filesystems may otherwise collapse or reject a checkout that worked on Windows.

## Suggested staged groups

Use `git add -n -- <paths>` before the real `git add -- <paths>` for every group.

1. **Repository control:** `AGENTS.md`, `README.md`, `.gitignore`, `.gitattributes`, `THIRD_PARTY_CONTENT.md`, `docs/research_program/`, `.agents/skills/`.
2. **Owned code and existing tracked changes:** inspect each source/script diff separately.
3. **Screening packages:** stage the four run paths named in the retention manifest, then confirm ignored caches did not enter.
4. **Manuscript evidence:** stage canonical ledgers, selected manuscripts/milestones, and the unignored v15 receipts/tools—not the entire audit archive.
5. **Otero corpus:** only after the data-rights decision, stage `database_fulltext_all/` separately so its size and file count are visible.

## Git/GitHub limits

- [ ] No ordinary Git object exceeds 100 MiB; review every object above 50 MiB.
- [ ] Keep each push below GitHub's 2 GiB push limit. Split code, research records, screening data, and corpus into separate commits/pushes if needed.
- [ ] Review directories above about 3,000 entries and paths near Windows limits.
- [ ] Do not configure LFS for thousands of small Markdown files without a measured benefit. Use it for qualifying large binary objects only and account for quota/bandwidth.
- [ ] Inspect `.gitattributes` normalization before staging large text corpora; the first normalization can make a large diff.

Official guidance: [repository limits](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits), [large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), and [Git LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs).

## Final dry run

- [ ] `git status --short` shows only intended modifications/untracked groups.
- [ ] `git diff --cached --stat` and `git diff --cached --name-status` match the retention manifest.
- [ ] `git ls-files` contains the three repo-local skills and required Otero/screening evidence.
- [ ] A fresh clone or worktree can open the project map and run the three read-only skill scripts.
- [ ] On macOS, install or select Python 3.10+ and run the clean-clone smoke tests below from the repository root. Keep `macos_runtime=unverified` until this target-OS run actually succeeds.
- [ ] No task transcript, `.env`, API response containing credentials, third-party cache, or ignored 6+ GiB pilot asset is staged.
- [ ] Push is performed manually by the owner.

```console
python3 .agents/skills/research-project-continuity/scripts/validate_requirement_registry.py --require-no-conflicts
python3 .agents/skills/research-project-continuity/scripts/audit_repository_readiness.py
python3 .agents/skills/coding-agent-manuscript/scripts/search_writing_prototypes.py --function theory-bridge --source ACAA-2024-ISR --limit 1
python3 .agents/skills/coding-agent-manuscript/scripts/audit_section_structure.py docs/research_program/current_state.md
python3 .agents/skills/ais-fulltext-screening/scripts/audit_screening_run.py --help
python3 .agents/skills/otero-open-api/scripts/download_fulltext.py --help
```
