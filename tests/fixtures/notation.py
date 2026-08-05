"""Notation fixture for the coding and writing standards."""


def project(x, X, W, hidden_states):
    """Project one vector and one matrix while preserving descriptive names."""
    n = len(x)
    X_projected = X[:n] @ W  # (n, d)
    embedding_vector = X_projected.mean(axis=0)  # (d,)
    hidden_states = hidden_states + X_projected  # (n, d)

    return embedding_vector, hidden_states
