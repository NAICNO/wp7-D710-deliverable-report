# UC2 — PEM Electrolyzer PINN Optimizer

```{objectives}
- Understand PEM electrolysis and why accurate voltage prediction matters
- Learn about the teacher-student knowledge distillation architecture
- See why 12 parameters beat ~530,000-parameter neural networks on OOD data
- Understand the digital twin and inverse pressure optimizer
```

**Repository:** [wp7-UC2-pem-electrolyzer-digital-twin](https://github.com/NAICNO/wp7-UC2-pem-electrolyzer-digital-twin)
**Tutorial:** [https://naicno.github.io/wp7-UC2-pem-electrolyzer-digital-twin/](https://naicno.github.io/wp7-UC2-pem-electrolyzer-digital-twin/)
**Contributors:** Hasan Asyari Arief (NORCE Research)

## The Problem

PEM (Proton Exchange Membrane) water electrolysis is a key technology for green hydrogen production. Predicting cell voltage under varying operating conditions is essential for safe, efficient operation.

The hard part is **generalization**: a model trained on one set of operating conditions must predict accurately when current, pressure, or temperature move outside the training range. Pure ML models fit training data well but fail when extrapolating. Purely empirical physics models lack the flexibility to capture the full behavior.

## Two-Stage Physics-Informed Architecture

### Stage 1: Teacher Model (HybridPhysicsMLP)

The teacher model embeds electrochemical equations directly into the network:

- **Nernst voltage** — thermodynamic equilibrium potential
- **Butler-Volmer activation** — overpotential from electrode kinetics
- **Ohmic losses** — membrane and electrode resistance

An MLP residual is clamped to ±100 mV so **physics always dominates**. The teacher has ~9,354 parameters.

### Stage 2: Student Model (PhysicsHybrid12Param)

Through knowledge distillation, a compact **12-parameter student model** learns from:
- Real experimental data (10% weight)
- Teacher's predictions (90% weight)

The student replaces the MLP with a 6-parameter logistic correction and adds a concentration overpotential term. This trades in-distribution fit for much better out-of-distribution generalization.

```{mermaid}
graph LR
    A[Real Data<br>10% weight] --> C[Student Loss]
    B[Teacher Predictions<br>90% weight] --> C
    C --> D[12-Parameter<br>Physics Model]
```

## The Biggest Takeaway: A 12-Number Equation

After training, the distilled student is **not a neural network**. It is a deterministic algebraic equation defined by exactly 12 scalar constants:

- 6 physics parameters (exchange currents, resistance, transfer coefficients, limiting current)
- 6 hybrid correction parameters (logistic curve + pressure/temperature modulation)

Anyone with these 12 numbers can reproduce the model's predictions in any language — Python, MATLAB, Excel — without PyTorch.

## Results

| Model | Parameters | Val MAE | OOD Avg MAE |
|-------|-----------|---------|-------------|
| **Distilled Student** | **12** | ~14 mV | **~15 mV** |
| Teacher (HybridPhysicsMLP) | ~9,354 | ~14 mV | ~28 mV |
| Pure Physics | 12 | ~25 mV | ~21 mV |
| PureMLP | ~2,049 | ~13 mV | ~42 mV |
| BigMLP | ~43,393 | ~12 mV | ~47 mV |
| Transformer | ~529,793 | ~10 mV | ~62 mV |

The pure ML models win on in-distribution validation because they have orders of magnitude more parameters to memorize training patterns. But they **collapse on out-of-distribution data**. The 12-parameter student outperforms the ~530K-parameter Transformer on OOD by over 4x.

## Beyond Prediction

UC2 also includes:

- **Inverse Pressure Optimizer**: Newton-Raphson with bisection fallback finds the maximum safe operating pressure for given conditions
- **Real-Time Digital Twin**: Combines PINN voltage predictions with Lattice-Boltzmann fluid dynamics at ~30 FPS, visualized in a 3D web interface

## Quick Start

```bash
git clone https://github.com/NAICNO/wp7-UC2-pem-electrolyzer-digital-twin.git
cd wp7-UC2-pem-electrolyzer-digital-twin
bash setup.sh
jupyter notebook demonstrator-v1.orchestrator.ipynb
```

The 9-chapter Sphinx tutorial makes UC2 one of the most thoroughly documented demonstrators in WP7.

```{keypoints}
- PINNs combine electrochemical physics with ML for better generalization
- Teacher-student knowledge distillation: teacher (~9K params) trains student (12 params)
- The 12-parameter student beats ~50K-parameter Transformers on OOD data by 5–6x
- After training, the student is a deterministic equation — reproducible from 12 numbers
- Includes inverse pressure optimizer and real-time digital twin with 3D visualization
```
