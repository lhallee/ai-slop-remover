---
name: apply-coding-standards
description: Review or convert existing working Python to the suite's coding standards without changing intended behavior. Use for explicit requests to apply the coding standards workflow, clean up awkward or AI-generated Python, organize imports, improve typing and control flow, add numerical shape traces, simplify module boundaries, or run focused and repository-scale style passes. Do not use as authorization to fix unrelated bugs or redesign public behavior.
---

# Apply Coding Standards

Make working Python easier to understand while preserving its behavior.

## Load the standards

Confirm that `../coding-standards/SKILL.md`, `../writing-standards/SKILL.md`, and `../apply-writing-standards/SKILL.md` exist. If any sibling is missing, stop and tell the user to install the complete four-skill suite.

Read `../coding-standards/SKILL.md` and every resource it requires before reviewing or editing.

## Select the mode and scope

- For **review**, **inspect**, or **critique**, report concrete findings without editing.
- For a snippet, file, module, diff, or pull request, limit work to that target and directly required tests or imports.
- For a package or repository pass, read `references/repository-pass.md` and inspect the complete requested first-party scope.

Default to the smallest scope that satisfies the request. Exclude generated, vendored, migration, build, and external code unless the user includes it.

Treat conversion as behavior-preserving unless the user explicitly requests a behavior change. Observable behavior includes exceptions, import side effects, CLI output, serialization, random-number use, dtype, device, tensor shape, and documented performance guarantees. Record unrelated bugs instead of silently fixing them.

## Establish the baseline

1. Read repository guidance and relevant configuration, including `AGENTS.md`, `CLAUDE.md`, `pyproject.toml`, and test configuration when present.
2. Identify the smallest existing test set that exercises the target.
3. Resolve the project-native Python and test commands once. Prefer the repository environment and configured runner.
4. On Windows, if no command is clear, resolve the directory containing this `SKILL.md`, run its `scripts/resolve_python.ps1` by absolute path once, and reuse the JSON result.
5. Run the selected baseline before behavior-relevant structural work.

Do not trigger downloads, CUDA, large datasets, remote machines, or slow integration suites unless the user requests them. Record pre-existing failures and compare like with like.

## Convert in two passes

First apply mechanical changes:

- organize imports and whitespace;
- improve domain names and useful type hints;
- remove narrative comments and dead indirection;
- apply the shared mathematical notation;
- add accurate and complete numerical shape traces.

Then make structural changes only when they materially improve ownership or data flow:

- remove unsupported speculative paths;
- extract a cohesive helper, object, or module;
- shorten orchestration into a visible sequence;
- update tests and only the documentation made stale by the change.

Run focused tests after each behavior-relevant structural batch. Do not weaken tests to make the conversion pass.

## Audit language

Run the sibling checker on touched Python and documentation when practical:

```text
python <absolute-writing-standards-dir>/scripts/audit_language.py <path>
```

Resolve `<absolute-writing-standards-dir>` from the sibling `writing-standards/SKILL.md`. Do not assume that the shell's working directory is a skill directory.

Treat its output as review prompts. Remove em dashes. Review flagged identifiers and prose in context. Preserve exact technical terms, public identifiers, literals, and external terminology.

## Review and report

Inspect the final diff for accidental behavior changes, stale imports, incorrect shape comments, unnecessary file movement, formatter conflicts, and duplicated explanations.

Report:

- scope inspected and files changed;
- what became simpler or clearer;
- baseline and final verification commands and outcomes;
- pre-existing failures and unverified behavior;
- retained complexity or narrow standards exceptions.

For repository-scale work, also report the coverage matrix from `references/repository-pass.md`.
