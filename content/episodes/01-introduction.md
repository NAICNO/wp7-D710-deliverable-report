# Introduction to NAIC WP7 Demonstrators

```{objectives}
- Understand what Work Package 7 delivers
- Learn about the seven use cases and their scientific domains
- Know where to find each repository and tutorial
- Understand the common infrastructure pattern
```

## Overview

The Norwegian AI Cloud (NAIC) promised that shared infrastructure could lower the barrier for researchers to apply machine learning in their own domains. Work Package 7 (WP7) tested that promise by building seven demonstrator projects, each solving a real research problem and each packaged as a self-contained pipeline that runs on NAIC Orchestrator VMs.

This deliverable — D7.10 — summarizes all seven demonstrators: their scientific contributions, methodology, infrastructure requirements, and current status.

## The Seven Use Cases

| UC | Title | Domain | Key Technique |
|----|-------|--------|---------------|
| **UC1** | Climate Indices Teleconnection | Climate Science | Ensemble ML (RF, XGBoost, MLP) |
| **UC2** | PEM Electrolyzer PINN Optimizer | Green Hydrogen | Physics-Informed Neural Networks |
| **UC3** | Pseudo-Hamiltonian Neural Networks | Dynamical Systems | Port-Hamiltonian Decomposition |
| **UC4** | 3D Medical Image Registration | Medical Imaging | ANTsPy + HD-BET |
| **UC5** | Graph-Based AIS Classification | Maritime Surveillance | Graph Neural Networks (DGL) |
| **UC6** | Multi-Modal Optimization | Optimization | Hybrid GA + CMA-ES |
| **UC7** | Latent PDE Representations | Scientific Computing | Autoencoders + Latent Alignment |

## Repositories

All repositories are hosted on GitHub under the NAICNO organization:

| UC | Repository | Tutorial |
|----|-----------|----------|
| UC1 | [wp7-UC1-climate-indices-teleconnection](https://github.com/NAICNO/wp7-UC1-climate-indices-teleconnection) | [Tutorial](https://naicno.github.io/wp7-UC1-climate-indices-teleconnection/) |
| UC2 | [wp7-UC2-pem-electrolyzer-digital-twin](https://github.com/NAICNO/wp7-UC2-pem-electrolyzer-digital-twin) | [Tutorial](https://naicno.github.io/wp7-UC2-pem-electrolyzer-digital-twin/) |
| UC3 | [wp7-UC3-pseudo-hamiltonian-neural-networks](https://github.com/NAICNO/wp7-UC3-pseudo-hamiltonian-neural-networks) | [Tutorial](https://naicno.github.io/wp7-UC3-pseudo-hamiltonian-neural-networks/) |
| UC4 | [wp7-UC4-medical-image-registration](https://github.com/NAICNO/wp7-UC4-medical-image-registration) | [Tutorial](https://naicno.github.io/wp7-UC4-medical-image-registration/) |
| UC5 | [wp7-UC5-ais-classification-gnn](https://github.com/NAICNO/wp7-UC5-ais-classification-gnn) | [Tutorial](https://naicno.github.io/wp7-UC5-ais-classification-gnn/) |
| UC6 | [wp7-UC6-multimodal-optimization](https://github.com/NAICNO/wp7-UC6-multimodal-optimization) | [Tutorial](https://naicno.github.io/wp7-UC6-multimodal-optimization/) |
| UC7 | [wp7-UC7-latent-pde-representation](https://github.com/NAICNO/wp7-UC7-latent-pde-representation) | [Tutorial](https://naicno.github.io/wp7-UC7-latent-pde-representation/) |

## Common Workflow

Every completed demonstrator follows the same operational pattern:

1. **Provision** a VM on [orchestrator.naic.no](https://orchestrator.naic.no/) with GPU support
2. **Clone** the repository and run the setup script
3. **Launch** Jupyter via SSH tunnel
4. **Run** the self-contained notebook end-to-end
5. **Inspect** results — figures, metrics, and saved models

This pattern means a researcher can go from `git clone` to results without managing infrastructure or installing complex dependencies manually.

## Technology Stack

| Technology | Use Cases | Role |
|------------|-----------|------|
| Python | All | Primary implementation language |
| PyTorch | UC2, UC3, UC5 | Deep learning framework |
| TensorFlow | UC7 | Deep learning framework |
| scikit-learn / XGBoost | UC1 | Classical ML and gradient boosting |
| DGL | UC5 | Graph neural network library |
| ANTsPy / HD-BET | UC4 | Medical image registration and brain extraction |
| CMA-ES / DEAP | UC6 | Evolutionary optimization |

## Infrastructure

| Infrastructure | Use Cases | Purpose |
|----------------|-----------|---------|
| NAIC Orchestrator VMs | All | GPU-enabled cloud VMs for interactive development |
| Jupyter Notebooks | All | Interactive demonstrator interfaces |
| Sphinx Tutorials (GitHub Pages) | All | Multi-chapter tutorial documentation |
| AI Agent Files | UC1, UC2, UC3, UC5, UC6, UC7 | AI coding assistant integration (AGENT.md) |

## Contributors

| Institution | Contributors | Use Cases |
|-------------|-------------|-----------|
| NORCE Research | Klaus Johannsen, Odd Helge Otterå, Adrian Evensen, Hasan Asyari Arief, Xue-Cheng Tai, Gro Fonnes, Nadine Goris, Bjørnar Jensen, Jerry Tjiputra, Yngve Heggelund | UC1, UC2, UC5, UC6, UC7 |
| SINTEF Digital | Sølve Eidnes, Kjetil Olsen Lye | UC3 |
| UiB | Saruar Alam | UC4 |

## What You Will Learn

| Episode | Topic |
|---------|-------|
| 02 | Provisioning a NAIC VM |
| 03 | Getting started with any use case |
| 04–10 | Detailed walkthrough of each use case |
| 11 | Cross-cutting patterns and lessons learned |
| 12 | FAQ |

```{keypoints}
- WP7 delivers seven self-contained ML demonstrators across diverse scientific domains
- All demonstrators run on NAIC Orchestrator VMs with GPU support
- Each repository includes data, code, environment specs, and a Jupyter notebook
- All demonstrators include Sphinx tutorials published on GitHub Pages
- Physics-informed approaches (UC2, UC3, UC7) generalize better with fewer parameters
- UC1 provides both interactive notebooks and CLI parameter sweeps
```
