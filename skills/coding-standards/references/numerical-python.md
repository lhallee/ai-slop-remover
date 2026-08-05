# Numerical Python standards

Apply this reference to NumPy, PyTorch, JAX, and similar array code in the selected scope.

## Use consistent symbols

- Use lowercase symbols for scalars and dimensions: `b` for batch, `l` for sequence length, `d` for hidden width, `h` for attention heads, `c` for classes, and `n` for a generic count.
- Use lowercase short symbols for vectors, such as `x`, `q`, and `v`.
- Use uppercase short symbols for matrices and tensors of rank two or greater, such as `X`, `W`, `Q`, `K`, and `V`.
- Use compound symbols when needed, such as `d_h` for per-head width.
- Define nonstandard symbols near their first use.
- Keep descriptive tensor names lowercase, such as `hidden_states`, `attention_mask`, and `logits`.
- Do not rename a clear descriptive tensor to a single letter merely to satisfy the convention.
- Preserve established domain notation when it is clearer for the intended reader.

Comment scalar dimension definitions that appear in later shapes:

```python
self.hidden_size = config.hidden_size  # d
self.num_heads = config.num_heads  # h
```

## Trace every shape

Annotate every array-valued binding or transformation so a reader can follow the full path without mentally executing the code. Include:

- function inputs;
- creation and assignment;
- reassignment and in-place mutation;
- layer and method calls;
- reshape, transpose, indexing, slicing, and masking;
- reductions, concatenation, stacking, and broadcasting;
- returned arrays and tensors.

Put the shape on the same line when practical:

```python
def forward(self, X: Tensor, attention_mask: Tensor) -> Tensor:
    # X: (b, l, d); attention_mask: (b, l)
    Q = self.query(X)  # (b, l, d)
    Q = Q.view(b, l, h, d_h)  # (b, l, h, d_h)
    Q = Q.transpose(1, 2)  # (b, h, l, d_h)
    scores = Q @ K.transpose(-2, -1)  # (b, h, l, l)
    hidden_states = scores @ V  # (b, h, l, d_h)
    X_pooled = hidden_states.mean(dim=(1, 2))  # (b, d_h)
    logits = self.classifier(X_pooled)  # (b, c)

    return logits  # (b, c)
```

Annotate a final binding once rather than every subexpression in a chained right-hand side. Include unchanged shapes after layer calls so the trace remains continuous. Use `()` for scalar arrays or tensors.

## Prefer accuracy over false certainty

Derive shapes from function contracts, layer configuration, tests, and upstream operations. Never copy a plausible shape without tracing it.

When a dimension is dynamic, give it a stable symbolic name and define that name. When rank or shape cannot be proven, express the uncertainty with a documented symbol or ellipsis and report the limitation. Treat a stale shape comment as a correctness defect.
