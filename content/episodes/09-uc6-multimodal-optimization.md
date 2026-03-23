# UC6 — Multi-Modal Optimization

```{objectives}
- Understand the multi-modal optimization problem: finding all optima, not just one
- Learn how SHGA combines Deterministic Crowding GA with CMA-ES
- See benchmark results on Himmelblau's function and CEC2013 suite
- Understand the parallelization strategy and NAIC multi-core benefits
```

**Repository:** [wp7-UC6-multimodal-optimization](https://github.com/NAICNO/wp7-UC6-multimodal-optimization)
**Tutorial:** [https://naicno.github.io/wp7-UC6-multimodal-optimization/](https://naicno.github.io/wp7-UC6-multimodal-optimization/)
**Contributors:** Klaus Johannsen, Noel Goris, Bjørn Jensen, Jerry Tjiputra (NORCE Research)
**Reference:** Johannsen, K., Goris, N., Jensen, B., & Tjiputra, J. (2022). *Nordic Machine Intelligence*, 02, 16–27. [DOI:10.5617/nmi.9633](https://doi.org/10.5617/nmi.9633)

## The Problem

Many real-world optimization problems in engineering design, molecular modeling, and scientific parameter estimation have **multiple valid solutions** — not just one global optimum.

Standard optimization algorithms converge to one solution and stop. Finding *all* optima requires strategies that balance:
- **Exploration** — searching the full domain
- **Exploitation** — refining promising regions

## SHGA: Scalable Hybrid Genetic Algorithm

UC6 implements SHGA, which combines two complementary strategies:

```{mermaid}
graph TD
    A[Initialize Population] --> B[Deterministic Crowding GA<br>Global exploration]
    B --> C[Nearest-Neighbor Clustering<br>Identify promising regions]
    C --> D[CMA-ES Refinement<br>Local precision per seed]
    D --> E{Found all optima?}
    E -->|No| F[Scale up population]
    F --> B
    E -->|Yes| G[Report all optima]
```

### Component 1: Deterministic Crowding GA

Handles **global exploration** while keeping population diversity. Individuals are replaced only by similar ones (nearest-neighbor replacement), preventing the population from collapsing onto a single solution.

### Component 2: CMA-ES Local Search

Once promising regions are identified through clustering, individual **CMA-ES** (Covariance Matrix Adaptation Evolution Strategy) instances refine each seed to high precision.

### Outer Loop

Scales up the population and repeats, progressively discovering additional optima.

## Parallelization

The inner CMA-ES loop is parallelized across available CPU cores:

| Cores | Speedup |
|-------|---------|
| 1 | 1x (baseline) |
| 4 | ~3x |
| 8 | ~3.5x |
| 16 | ~3.8x |

This yields **3–4x speedup** on 16-core NAIC Orchestrator VMs, showing that NAIC infrastructure benefits workloads beyond deep learning.

## Results

### Himmelblau's Function

SHGA reliably discovers all **4 global optima** of Himmelblau's function within 50,000 evaluations:

| Optimum | Location (x, y) | f(x, y) |
|---------|-----------------|---------|
| 1 | (3.0, 2.0) | 0.0 |
| 2 | (-2.805, 3.131) | 0.0 |
| 3 | (-3.779, -3.283) | 0.0 |
| 4 | (3.584, -1.848) | 0.0 |

### CEC2013 Benchmark Suite

Average **peak ratio of 66%** across the 20-function CEC2013 benchmark suite (2–20 dimensions). Peak ratio measures the fraction of known global optima found.

## Key Dependencies

| Package | Role |
|---------|------|
| DEAP | Evolutionary algorithm framework (GA operators) |
| CMA-ES | Local optimization (covariance matrix adaptation) |
| NumPy | Numerical operations |
| Matplotlib | Visualization |

## Quick Start

```bash
git clone https://github.com/NAICNO/wp7-UC6-multimodal-optimization.git
cd multi-modal-optimization
pip install -r requirements.txt
jupyter notebook demonstrator-v1.orchestrator.ipynb
```

The self-contained orchestrator notebook runs SHGA on CEC2013 F1–F7 benchmarks with synthetic data, demonstrating the algorithm's ability to find multiple optima.

```{keypoints}
- Multi-modal optimization finds all optima, not just one global optimum
- SHGA combines Deterministic Crowding GA (exploration) with CMA-ES (exploitation)
- Reliably discovers all 4 optima of Himmelblau's function within 50K evaluations
- 66% average peak ratio on the CEC2013 20-function benchmark suite
- Parallelized CMA-ES achieves 3–4x speedup on 16-core NAIC VMs
- Based on prior work published in Nordic Machine Intelligence (2022)
```
