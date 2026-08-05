# Repository-scale coding pass

Read this reference only for a package-wide or repository-wide conversion.

## Inventory the scope

Inspect every relevant first-party Python module in the requested packages, applications, examples, and tests. Exclude generated, vendored, migration, build, and explicitly out-of-scope files.

Before editing, classify each eligible file as:

- `compliant`
- `mechanical edit`
- `structural edit`
- `excluded` with a reason
- `blocked` with a reason

Do not present a representative sample as complete coverage.

## Stage the work

1. **Baseline:** read repository guidance, resolve commands, run focused CPU tests, and map dependencies.
2. **Mechanical pass:** apply imports, spacing, naming, useful types, comments, notation, and numerical shape traces.
3. **Structural pass:** make only justified extractions, module splits, object boundaries, and entry-point simplifications.
4. **Synchronization pass:** update affected tests and only documentation made stale by the conversion.
5. **Verification pass:** run focused tests after structural batches, run the agreed final checks, audit language, and review the full diff.

Batch compatible edits by module. Avoid repository-wide formatter churn outside the classified scope.

## Use independent review when useful

For substantial or risky changes, assign non-overlapping review roles such as behavior preservation, typing and data flow, module ownership, tests, and documentation. Require actionable findings. Do not create reviewer overhead for a small focused pass.

## Close the inventory

Report files inspected, changed, already compliant, excluded, and blocked. Include baseline and final verification results and material reviewer recommendations rejected because they conflicted with correctness or scope.
