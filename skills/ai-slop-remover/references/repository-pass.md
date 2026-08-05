# Repository-scale pass

Read this reference only when the user requests a package-wide or repository-wide cleanup.

## Inventory the scope

Inspect every relevant first-party Python module in the requested packages, applications, examples, and tests. Exclude generated, vendored, migration, build, and explicitly out-of-scope files.

Before editing, create a compact file-by-file matrix:

- `compliant`
- `mechanical edit`
- `structural edit`
- `excluded` with reason
- `blocked` with reason

Do not stop after a few representative files. Work through every eligible file marked for editing, and never call a partial pass comprehensive.

## Stage the work

1. **Bootstrap:** read repository guidance, resolve the Python and test commands once, run the smallest relevant CPU baseline, and map dependencies.
2. **Mechanical pass:** apply import order, spacing, naming, useful types, comments, and numerical shape traces.
3. **Structural pass:** make only justified extractions, module splits, object boundaries, and entry-point simplifications.
4. **Synchronization pass:** update affected tests and only the documentation made stale by module, interface, configuration, or workflow changes.
5. **Verification pass:** run focused tests after structural batches, then run the agreed final command set and review the full diff.

Batch compatible edits by module. Avoid repository-wide formatting churn outside the matrix.

## Use independent reviewers selectively

When subagents are available and the scope materially benefits, assign non-overlapping reviews:

- style and formatting;
- design, typing, and data flow;
- module ownership and dependency direction;
- tests and behavior-preservation risk;
- documentation synchronization.

Combine roles for modest packages. Require actionable, file-specific findings. Do not make five reviewers mandatory when one or two independent passes cover the risk.

## Close the matrix

At completion, report:

- files inspected;
- files changed;
- files already compliant;
- files excluded and why;
- files blocked and the exact decision needed;
- baseline and final verification results;
- material reviewer recommendations rejected and why.

Do not defer a selected numerical module merely because shape tracing is substantial. Complete the trace, narrow the scope with the user's agreement, or mark the file blocked with a concrete reason.
