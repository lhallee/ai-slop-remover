# Notation fixture

Let (n) be the number of samples, (d) the feature dimension, and (x \in \mathbb{R}^{d}) one feature vector. The matrix (X \in \mathbb{R}^{n \times d}) contains all samples. A rank-three tensor (H \in \mathbb{R}^{b \times l \times d}) contains a batch of sequences. Mean pooling over the batch and sequence dimensions reduces (H) to the vector (h \in \mathbb{R}^{d}).

**Figure 1.** The tensor (H) has shape ((b, l, d)); the reduced vector (h) has shape ((d,)). The descriptive identifier `hidden_states` follows lowercase snake case even when it names (H).
