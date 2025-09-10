# UC3 — Pseudo-Hamiltonian Neural Networks

```{objectives}
- Understand why standard neural networks fail at long-horizon dynamical system modeling
- Learn about port-Hamiltonian decomposition into conservation, dissipation, and external forces
- See how physics structure enables interpretability and out-of-distribution generalization
- Know the status of SINTEF's phlearn package integration
```

**Repository:** [wp7-UC3-pseudo-hamiltonian-neural-networks](https://github.com/NAICNO/wp7-UC3-pseudo-hamiltonian-neural-networks)
**Reference Implementation:** [github.com/SINTEF/pseudo-hamiltonian-neural-networks](https://github.com/SINTEF/pseudo-hamiltonian-neural-networks)
**Contributors:** Sølve Eidnes, Kjetil Olsen Lye (SINTEF Digital)

## The Problem

Standard neural networks trained to model physical systems learn to predict the next state but have no built-in notion of:
- **Energy conservation** — total energy should be preserved in closed systems
- **Dissipation** — energy should decay predictably due to friction and damping
- **External forcing** — energy input from external sources should be separated

Without these constraints, neural networks can produce physically implausible trajectories, especially over long time horizons.

## Approach: Port-Hamiltonian Decomposition

UC3 decomposes system dynamics into three physically meaningful components, each modeled by a separate sub-network:

```{mermaid}
graph TD
    A[System State x] --> B[Conservation Network<br>Energy-preserving Hamiltonian]
    A --> C[Dissipation Network<br>Energy loss and damping]
    A --> D[External Force Network<br>State-dependent forcing]
    B --> E[dx/dt]
    C --> E
    D --> E
```

| Component | Physics Role | Sub-Network |
|-----------|-------------|-------------|
| Conservation | Energy-preserving Hamiltonian dynamics | Skew-symmetric structure |
| Dissipation | Energy loss (friction, damping) | Positive semi-definite structure |
| External Force | State-dependent forcing terms | General neural network |

This decomposition is rooted in **port-Hamiltonian theory** and ensures that each learned component is physically interpretable. A researcher can inspect what the model attributes to dissipation versus external forcing, for example.

## Key Innovations

- **Symmetric fourth-order integration schemes** improve training with sparse and noisy data
- **Decomposable architecture** means each component can be inspected independently
- **Modified dynamics**: learned models remain valid when external forces are changed or removed — standard neural networks cannot do this

## Results

The approach outperforms standard neural networks on dynamical systems benchmarks:

| Benchmark | Description |
|-----------|------------|
| Forced/damped mass-spring | Classical mechanics with dissipation |
| Complex tank systems | Fluid dynamics with multiple interacting tanks |
| PDEs | Partial differential equations with conservation laws |

Reference publications (prior work by SINTEF):
- Eidnes et al., *Journal of Computational Physics* (2023)
- Eidnes et al., *Applied Mathematics and Computation* (2024)

## The phlearn Package

The reference implementation is maintained by SINTEF as the open-source `phlearn` Python package:

```bash
pip install -e phlearn/
```

The package provides:
- Pre-built PHNN architectures
- Training loops with physics-aware losses
- Integration schemes (symplectic, symmetric fourth-order)
- Example notebooks for standard benchmarks

## Status

UC3 is led by SINTEF, building on their prior research. The WP7 repository integrates the `phlearn` package with a full test suite and CI/CD pipeline.

Like UC2, UC3 shows that **embedding physics into the architecture produces models that generalize better** than pure data-driven alternatives.

## Quick Start

```bash
git clone https://github.com/NAICNO/wp7-UC3-pseudo-hamiltonian-neural-networks.git
cd pseudo-hamiltonian-neural-networks
pip install -e phlearn/
pytest tests/ -v
```

```{keypoints}
- Standard neural networks lack notions of energy conservation, dissipation, and forcing
- PHNNs decompose dynamics into three physically interpretable components
- Port-Hamiltonian structure ensures each component has the correct mathematical properties
- Learned models remain valid when external forces are modified or removed
- Based on prior work published in Journal of Computational Physics (2023) and Applied Mathematics and Computation (2024)
- The phlearn package provides ready-to-use PHNN architectures and training utilities
```
