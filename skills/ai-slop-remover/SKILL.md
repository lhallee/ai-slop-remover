---
name: ai-slop-remover
description: Review or refactor already-working Python into Logan's direct, readable, team-oriented style without changing intended behavior. Write all documentation and Markdown in ASD-STE100 Simplified Technical English, and apply the same rules concisely to code comments. Use for awkward or AI-generated Python, over-general helpers, import cleanup, precise typing, control-flow readability, NumPy/PyTorch tensor-shape traces, documentation cleanup, module boundaries, thin entry points, or focused and repository-scale style passes. Do not use as authorization to fix unrelated bugs or redesign public behavior.
---

# AI Slop Remover

Make correct Python easier for a human maintainer to understand. Prefer direct code, domain language, and visible data flow over cleverness, speculative generality, or abstraction for its own sake.

## Apply the preference hierarchy

Resolve conflicts in this order:

1. Follow the user's explicit scope and requested behavior.
2. Preserve correctness, security, public interfaces, data schemas, and tested behavior.
3. Follow repository instructions and enforced formatter, linter, and type-checker configuration.
4. Apply the preferences in this skill.
5. Minimize unrelated diff churn.

Treat a style refactor as behavior-preserving unless the user explicitly requests otherwise. Observable behavior includes exceptions, import side effects, CLI output, serialization, random-number use, dtype, device, tensor shape, and documented performance guarantees. If a preference conflicts with a higher-priority constraint, keep the narrow exception and report it. Do not silently fix unrelated bugs discovered during cleanup.

## Choose the right scope

Infer the mode from the request:

- For **review**, **inspect**, or **critique**, report concrete findings without editing.
- For a snippet, file, named module, diff, or PR, limit work to that target and any directly required tests or imports.
- For a package or repository cleanup, inspect the full requested first-party scope. Read [repository-pass.md](references/repository-pass.md) before editing.

Never turn an ambiguous cleanup request into a repository-wide rewrite. Default to the smallest scope that fully addresses the supplied code or named target. Exclude generated, vendored, migration, build, and external code unless the user includes it.

## Establish behavior before editing

1. Read repository guidance and tool configuration relevant to the target, including `AGENTS.md`, `CLAUDE.md`, `pyproject.toml`, and test configuration when present.
2. Identify the smallest existing test set that exercises the target.
3. Resolve the project-native Python command once and reuse it. Prefer the repository environment and configured runner such as `uv`, `tox`, `nox`, or Poetry. On Windows, if no working command is clear, resolve the bundled script relative to this `SKILL.md`, run `powershell -ExecutionPolicy Bypass -File <skill-dir>/scripts/resolve_python.ps1 -ProjectPath <repo>` once, and cache its JSON result.
4. Run the selected tests before behavior-affecting structural edits, then run the same tests afterward.

Keep validation proportional:

- For imports, comments, annotations, and other mechanical edits, use the relevant formatter, linter, type checker, compile check, or focused tests already available.
- For structural edits, require a meaningful behavioral baseline. If no relevant tests exist, add focused CPU-only characterization tests when that is within scope. Otherwise restrict the change to low-risk cleanup and state the limitation.
- Freeze baseline commands and expectations before editing. Do not weaken tests to make the refactor pass. Keep new characterization tests separate from the unchanged baseline comparison.
- Record pre-existing failures instead of claiming a clean baseline. Compare like with like after editing, and run all repository-native checks affected by a structural change.
- Do not trigger downloads, CUDA, large datasets, remote machines, or slow integration suites unless the user requests them.
- Treat an SSH host-key change as a security decision. Require explicit confirmation against an independently verified fingerprint.

## Refactor in two passes

Apply safe mechanical improvements first:

- organize imports and whitespace;
- improve names, useful type hints, and intent comments;
- remove obvious narrative comments and dead indirection;
- add accurate tensor-shape traces when numerical arrays are present.

Then make structural changes only where they materially improve ownership or data flow:

- collapse speculative branches and unsupported compatibility paths;
- extract a cohesive helper, object, or module;
- shorten orchestration into a visible sequential workflow;
- update tests and documentation only when the resulting interface, module boundary, configuration, or workflow changed.

Run focused tests after each behavior-relevant structural batch. Review the final diff for accidental behavior changes, unnecessary file movement, formatter conflicts, and stale imports.

## Organize imports in Logan's order

Keep a module docstring first and any `from __future__ import ...` statements immediately after it. Then put every direct `import ...` statement before every ordinary `from ... import ...` statement. Within those two blocks, keep standard-library names before third-party names. Put repository-local imports in a distinct final section.

```python
import argparse
import numpy as np
import torch
from torch import Tensor
from pathlib import Path

from .workflow import TrainingWorkflow
```

Leave two blank lines after the complete import block before module configuration or the first definition. Keep descriptive all-caps configuration near the top of runnable modules.

Preserve guarded, optional, registration, and initialization-sensitive import order. Treat these as ordering barriers rather than moving imports across them.

Do not fight an enforced formatter that produces a different order. Keep its output and report the conflict, or update formatter configuration only when the user asks.

## Prefer direct functions and control flow

- Give each function one narrow, typed responsibility.
- Add precise parameter and return types. Add attribute or local annotations when they clarify a non-obvious type or help the configured type checker.
- Prefer concrete domain types and parameterized containers. Use `Any` only at a genuinely dynamic boundary.
- Respect the project's minimum Python version and typing conventions. Do not change framework-discovered fields, runtime annotation behavior, import cycles, or serialization schemas merely to add types.
- Code for supported, well-typed inputs. Remove speculative support and defensive branches only after confirming they do not protect a real requirement.
- Raise ordinary exceptions for invalid external input. Use assertions for internal invariants and programmer assumptions. Add no quota-driven assertions.
- Separate distinct guards, loops, exception handling, and logical phases with blank lines when it improves scanning.
- Keep parser declarations on one line when they remain comfortable to read.
- Avoid broad `except Exception`, silent fallback cascades, compatibility shims without a supported caller, and wrappers that merely rename one call.
- Extract a one-use helper only when naming a real concept or isolating a separately testable phase makes the caller clearer.

## Write for maintainers

- Use domain-specific names. Avoid vague names such as `data`, `result`, `info`, or `manager` when the domain supplies a better term.
- Write all documentation in ASD-STE100 Simplified Technical English (STE). This requirement includes all Markdown files, README files, guides, docstrings, API documentation, examples, and user-facing technical instructions that you create or edit.
- When documentation is in scope, apply STE to the complete document. Do not apply it only to the text that you add. Do not expand the task to unrelated documents.
- Use the current ASD-STE100 writing rules and controlled dictionary. Use an approved word only with its approved meaning and part of speech. Prefer one word for one meaning. Use short, direct sentences and simple verb forms. Use American English spelling. Use established project and domain terms as technical nouns or technical verbs when STE permits them.
- Preserve code identifiers, commands, paths, literal values, quoted interface text, and required external terminology. Do not change them only to satisfy STE.
- Make code comments follow STE vocabulary and grammar as closely as practical. Keep comments concise. A short comment can omit articles or other words when the full STE sentence would add noise, but it must stay clear and unambiguous.
- Comment intent, assumptions, units, biological conventions, non-obvious mechanics, and design rationale.
- Remove comments and docstrings that only narrate syntax or repeat a precise name and type.
- Keep comments close to the code they qualify.
- Verify that an API is actually deprecated before replacing it.
- Preserve meaningful safeguards, but make their scope explicit and their implementation proportional.

## Trace numerical shapes

For NumPy, PyTorch, JAX, or similar array code, read and apply [numerical-python.md](references/numerical-python.md). Treat its shape-trace convention as required for the selected numerical module, while never inventing a shape that the code or contract cannot support.

## Keep structure cohesive

- Give each module one primary responsibility, not one arbitrary kind of statement.
- Split by ownership and dependency direction, never by line count alone.
- Keep reusable helpers near their owning feature. Do not create catch-all `utils.py` modules.
- Give extracted modules a small intentional public surface. Avoid circular imports and implicit shared state.
- Use a class when state and behavior form a meaningful domain object or workflow. Prefer a function, typed value, or dataclass for simple transformations and records.
- Keep entry points thin: parse arguments, construct configuration and collaborators, then invoke a short sequence whose names expose the workflow.
- Prefer visible steps such as `load`, `validate`, `step`, and `save` over dense orchestration or framework-like indirection.

## Review efficiently

Use an independent review pass when the change is structurally substantial, spans several modules, or has meaningful behavior-preservation risk. Give reviewers the code and test contract, not a desired conclusion. Partition file ownership if reviewers edit. For a small focused cleanup, perform one careful self-review instead of creating reviewer overhead.

Accept only findings that improve compliance without changing behavior or expanding scope. Report any material recommendation rejected because it conflicted with correctness, tests, repository constraints, or the user's request.

## Finish with evidence

Report:

- the scope inspected and files changed;
- what became simpler, clearer, or more cohesive;
- the baseline and final verification commands and outcomes;
- any pre-existing failures, unverified behavior, retained complexity, or narrow preference exceptions.

For repository-scale work, also report the coverage matrix described in [repository-pass.md](references/repository-pass.md). Never describe a partial pass as comprehensive.
