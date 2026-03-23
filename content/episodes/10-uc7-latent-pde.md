# UC7 — Latent Representation of PDE Solutions

```{objectives}
- Understand why re-solving PDEs for every parameter configuration is expensive
- Learn about the autoencoder-based approach to learning solution manifolds
- See how cross-modal latent alignment bridges parameters and solutions
- Understand how the framework handles multiple grid discretizations
```

**Repository:** [wp7-UC7-latent-pde-representation](https://github.com/NAICNO/wp7-UC7-latent-pde-representation)
**Contributors:** Klaus Johannsen, Yngve Heggelund (NORCE Research)

## The Problem

Solving partial differential equations (PDEs) numerically is expensive. For applications that require exploring a **parameterized family of solutions** — varying boundary conditions, coefficients, or discretization resolutions — re-solving the PDE for every parameter configuration is prohibitive.

UC7 tackles this by learning a compact representation of the entire solution manifold, so that new solutions can be evaluated, interpolated, and compared **without running the solver**.

## Approach: Three-Stage Latent Learning

UC7 focuses on **steady-state convection–diffusion equations** in two spatial dimensions, with parameterized, divergence-free convection fields.

```{mermaid}
graph LR
    subgraph "Stage 1: Train Separately"
        A[Solution Fields] --> B[Solution<br>Autoencoder]
        C[Streamfunction<br>Parameters] --> D[Parameter<br>Autoencoder]
    end
    subgraph "Stage 2: Align"
        B --> E[Shared Latent Space]
        D --> E
    end
    subgraph "Stage 3: Fine-tune"
        E --> F[Cross-Modal<br>Reconstruction]
    end
```

### Stage 1: Train Autoencoders Separately

Train autoencoders on two modalities independently:
- **Solution autoencoder** — learns compact representations of PDE solution fields
- **Parameter autoencoder** — learns compact representations of the convection streamfunction

### Stage 2: Align Latent Spaces

Align the latent spaces of these different modalities so that a single shared representation bridges between parameters and solutions.

### Stage 3: Fine-tune

Fine-tune encoders and decoders toward the shared latent, then evaluate reconstruction quality via relative MSE across modalities and grid discretizations.

## Key Capabilities

| Capability | Description |
|-----------|-------------|
| **Cross-modal transfer** | Map from parameter space to solution space without solving the PDE |
| **Multi-resolution** | Multiple grid discretizations coexist within the same latent space |
| **Interpolation** | Generate new solutions for parameter values not in the training set |
| **Compression** | Compact latent representations reduce storage and computation |

## What It Found

The framework learns structured latent spaces that capture the solution manifold:
- Cross-modal alignment enables transfer between parameter space and solution space
- Multiple grid discretizations coexist within the same latent space, meaning the representation works regardless of mesh resolution
- The approach bridges parameters and solutions through a shared learned geometry

## Educational Value

UC7 is designed as an **educational sandbox** for researchers interested in:
- Neural operators for scientific computing
- Representation learning for PDE solutions
- Autoencoder architectures for scientific data
- Latent space alignment across different modalities

It is the third use case (alongside UC2 and UC3) where the ML approach is shaped by the structure of the underlying mathematics, instead of treating the problem as generic regression.

## Key Dependencies

| Package | Role |
|---------|------|
| TensorFlow | Deep learning framework (autoencoders) |
| NumPy | Numerical operations |
| SciPy | Sparse matrices, PDE solver |
| Matplotlib | Visualization |

## Quick Start

```bash
git clone https://github.com/NAICNO/wp7-UC7-latent-pde-representation.git
cd latent-representation-of-pde-solutions
pip install -r requirements.txt
jupyter notebook demonstrator-v1.orchestrator.ipynb
```

```{keypoints}
- Re-solving PDEs for every parameter configuration is computationally prohibitive
- Autoencoders learn compact representations of PDE solutions and parameters separately
- Latent space alignment creates a shared representation bridging parameters and solutions
- Cross-modal transfer: map from parameters to solutions without running the solver
- Multiple grid discretizations coexist in the same latent space
- Educational sandbox for neural operators and representation learning
```
