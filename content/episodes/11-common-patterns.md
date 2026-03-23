# Cross-Cutting Patterns and Lessons Learned

```{objectives}
- Identify common themes across the seven demonstrators
- Understand why physics-informed ML generalizes better with fewer parameters
- See how data representation choices affect model performance
- Learn how NAIC infrastructure bridges interactive and batch computing
- Understand the reproducibility pattern used across all repositories
```

## Pattern 1: Physics-Informed ML Generalizes Better with Fewer Parameters

Three use cases embed domain physics directly into their neural architectures:

| UC | Technique | Finding |
|----|-----------|---------|
| UC2 | Electrochemical equations in network | 12-param student beats ~50K-param Transformer on OOD |
| UC3 | Port-Hamiltonian decomposition | Models remain valid when forces are modified |
| UC7 | PDE-structured latent spaces | Cross-modal alignment works across discretizations |

The pattern is consistent: **embedding physics into the architecture** produces models that generalize better with far fewer parameters. The pure ML models win on in-distribution validation because they have orders of magnitude more parameters to memorize training patterns, but they collapse on out-of-distribution data.

This has practical implications. Smaller models:
- Are cheaper to train and deploy
- Have interpretable parameters (UC2's 12 numbers can be inspected individually)
- Can be validated against known physics
- Degrade gracefully outside the training distribution

## Pattern 2: Data Representation Matters as Much as Model Choice

Two use cases showed that how you represent the data matters as much as which model you use:

| UC | Representation Choice | Impact |
|----|----------------------|--------|
| UC5 | Graphs instead of flat time series | Captured spatial-temporal vessel patterns |
| UC7 | Multi-modal autoencoders with alignment | Bridged parameter and solution spaces |

In UC5, all three GNN architectures (GCN, GraphSAGE, GAT) achieved over 92% accuracy — the performance gap between architectures was smaller than the gap between graph and non-graph representations. The structural decision dominated the model decision.

## Pattern 3: NAIC Infrastructure Bridges Interactive and Batch Computing

UC1 demonstrates the clearest example:

| Workflow | Platform | Use Case |
|----------|---------|----------|
| Interactive exploration | NAIC Orchestrator VM | Single-target analysis, parameter tuning |
| Large-scale sweeps | Sigma2 HPC (SLURM) | 42,613 experiments across all combinations |

UC2 and UC6 show how Orchestrator VMs with GPU and multi-core support handle training workloads that would be impractical on a researcher's laptop:

- UC2: GPU training for teacher and student models
- UC6: 3–4x speedup from multi-core parallelized CMA-ES

The shared pattern of SSH-tunneled Jupyter access, tmux-based background training, and one-command setup scripts cuts the operational overhead for domain scientists.

## Pattern 4: Reproducibility Through Self-Contained Repositories

Every completed demonstrator ships as a Git repository containing:

| Component | Purpose |
|-----------|---------|
| Data (or download scripts) | Training and evaluation data |
| Environment specifications | `requirements.txt`, `environment.yml`, `setup.sh` |
| Training code | Scripts and utility modules |
| Evaluation scripts | Metrics computation and visualization |
| Jupyter notebook | End-to-end interactive demonstration |
| Test suite | Automated validation (CI/CD) |

All demonstrators additionally include **Sphinx tutorials** published on GitLab Pages, and six (all except UC4) include **AGENT.md files** for AI coding assistant integration.

A new researcher can go from `git clone` to results without external dependencies.

## Pattern 5: Lean CI for Heavy Workloads

All seven repositories now include GitLab CI/CD pipelines that:
- Run on `python:3.11-slim` Docker images
- Use lean `requirements-test.txt` (no GPU frameworks)
- Skip tests gracefully when heavy dependencies are unavailable
- Validate project structure, notebook validity, and code quality
- Deploy Sphinx documentation to GitLab Pages

This approach means CI runs in seconds, not minutes, while still catching structural and code issues.

## Deviations and Status

| UC | Status | Notes |
|----|--------|-------|
| UC1 | **Completed** | Full tutorial, CLI, dual-platform support |
| UC2 | **Completed** | 9-chapter tutorial, digital twin, AGENT.md |
| UC3 | **Completed** | phlearn package, test suite, CI/CD pipeline |
| UC4 | **Completed** | Registration pipeline, orchestrator notebook, test suite, CI/CD |
| UC5 | **Completed** | Full GNN framework, YAML-based configuration |
| UC6 | **Completed** | Tutorial, parallelization, published in NMI |
| UC7 | **Completed** | Autoencoder framework, educational sandbox |

```{note}
UC7 uses an MIT license, while the other WP7 repositories follow the dual CC BY-NC 4.0 (content) + GPL-3.0-only (code) standard. This will be updated for consistency.
```

```{keypoints}
- Physics-informed architectures consistently outperform pure ML on out-of-distribution data
- Data representation choices can matter more than model architecture choices
- NAIC infrastructure enables both interactive exploration and batch-scale experiments
- Self-contained repositories with setup scripts enable `git clone` to results
- Lean CI/CD pipelines validate structure and code without requiring GPU
```
