# Numerical Python preferences

Apply this reference to NumPy, PyTorch, JAX, and similar array code in the selected scope.

## Shape notation

- Use lowercase symbols for dimensions: `b` for batch, `l` for sequence length, `d` for hidden width, `h` for attention heads, `c` for classes, and `n` for a generic count.
- Define nonstandard symbols near their first use. Use literal sizes when fixed and useful.
- Use compound symbols when needed, such as `d_h` for per-head width.
- Comment scalar dimension definitions that appear in later shapes:

```python
self.hidden_size = config.hidden_size  # d
self.num_heads = config.num_heads  # h
```

## Complete shape traces

Annotate every tensor-valued binding or transformation so a reader can follow the full path without mentally executing the code. Include:

- function inputs;
- creation and assignment;
- reassignment and in-place mutation;
- layer and method calls;
- reshape, transpose, indexing, slicing, and masking;
- reductions, concatenation, stacking, and broadcasting;
- returned tensors.

Put the comment on the same line as the expression when practical:

```python
def forward(self, X: Tensor, attention_mask: Tensor) -> Tensor:
    # X: (b, l, d); attention_mask: (b, l)
    Q = self.query(X)  # (b, l, d)
    Q = Q.view(b, l, h, d_h)  # (b, l, h, d_h)
    Q = Q.transpose(1, 2)  # (b, h, l, d_h)
    scores = Q @ K.transpose(-2, -1)  # (b, h, l, l)
    pooled = hidden_states.mean(dim=1)  # (b, d)
    logits = self.classifier(pooled)  # (b, c)

    return logits  # (b, c)
```

Annotate a final binding once rather than every subexpression in a chained right-hand side. Include unchanged shapes after layer calls so the trace remains continuous. Use `()` for scalar arrays or tensors.

## Accuracy over false certainty

Derive shapes from function contracts, layer configuration, tests, and upstream operations. Never copy a plausible-looking comment without tracing it.

When a dimension is dynamic, give it a stable symbolic name and define that name. When the code supports variable rank or a dimension cannot be proven, express that uncertainty honestly with a documented symbol or ellipsis and report the limitation. Do not fabricate a fixed shape to satisfy the convention.

Keep comments synchronized when code changes. Treat a stale shape comment as a correctness defect.

## Tensor names

- Use uppercase single-letter names for mathematical matrices and tensors, such as `X`, `W_q` (W is reserved for weights), `Q`, `W_k`, `K`, `W_v`, and `V`.
- Keep descriptive tensor names lowercase, such as `hidden_states`, `attention_mask`, `logits`, and `output`.
- Do not rename a clear descriptive tensor to a single letter merely to satisfy the convention.
- Preserve established domain notation when it is more recognizable to the intended reader.
