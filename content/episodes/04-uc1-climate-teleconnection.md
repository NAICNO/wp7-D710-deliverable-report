# UC1 — Climate Indices Teleconnection Analysis

```{objectives}
- Understand what climate teleconnections are and why ML is useful for discovering them
- Learn about the NorESM1-F simulation data and the 65 climate indices
- Understand the ML pipeline: lagged features, ensemble models, wavelet filtering
- Know how to run both interactive (Orchestrator) and batch (Sigma2 HPC) workflows
```

**Repository:** [wp7-UC1-climate-indices-teleconnection](https://github.com/NAICNO/wp7-UC1-climate-indices-teleconnection)
**Tutorial:** [https://naicno.github.io/wp7-UC1-climate-indices-teleconnection/](https://naicno.github.io/wp7-UC1-climate-indices-teleconnection/)
**Contributors:** Klaus Johannsen, Adrian Evensen, Hasan Asyari Arief (NORCE Research), Lorand Szentannai (Sigma2)

## The Problem

Climate teleconnections are large-scale patterns that link distant regions' weather and climate. They are central to decadal climate prediction, but identifying them from observational data is hard. Traditional approaches rely on expert-curated index pairs and linear statistics.

UC1 tests whether machine learning can systematically discover teleconnection relationships across a large set of climate indices — including non-linear ones — and use them for multi-decadal forecasts.

## Data

The team worked with three long-term climate simulations from the Norwegian Earth System Model (NorESM1-F), spanning 850–2005 AD under different forcing scenarios:

| Simulation | Forcing | Period |
|-----------|---------|--------|
| Low Solar | Reduced solar irradiance | 850–2005 AD |
| High Solar | Enhanced solar irradiance | 850–2005 AD |
| Pre-industrial Control | Constant forcing | 1000 years |

These simulations provide **65 climate indices** covering:
- Surface temperatures
- Sea surface temperatures
- Sea ice concentration
- Precipitation
- Atmospheric pressure
- Ocean circulation

## ML Pipeline

```{mermaid}
graph LR
    A[65 Climate Indices] --> B[Normalize 0-100]
    B --> C[Generate Lagged Features<br>up to 150-year lags]
    C --> D[Train Ensemble Models]
    D --> E[Feature Importance]
    E --> F[Top-N Selection]
    F --> G[Evaluate: Pearson r + MAE]
```

The framework:
1. Normalizes all indices to a 0–100 scale
2. Generates lagged features to capture temporal dependencies (up to 150-year lags)
3. Trains an ensemble of five model types:

| Model | Type |
|-------|------|
| Linear Regression | Baseline |
| Random Forest | Ensemble |
| XGBoost | Gradient Boosting |
| MLP | Neural Network |
| LRforcedPSO | PSO-constrained Linear Regression |

4. Feature importance is averaged across ensemble runs, top-N features are selected
5. Performance is evaluated using Pearson correlation and MAE
6. An optional Morlet wavelet bandpass filter isolates specific frequency bands

## Results

Over **42,613 individual experiments** were conducted across all model–target–lag combinations:

- ML models achieved correlation coefficients exceeding **0.7** for more than 20 target climate indices
- Statistically significant teleconnections identified across multi-decadal timescales
- Results support **10–50 year forecasts** of patterns such as Atlantic Multidecadal Variability (AMV) and Pacific Decadal Variability (PDV)

## Dual Infrastructure

UC1 is the only demonstrator that runs on **both** platforms:

| Platform | Notebook | Use Case |
|----------|---------|----------|
| NAIC Orchestrator | `demonstrator-v1.orchestrator.ipynb` | Interactive exploration |
| Sigma2 HPC (SLURM) | `demonstrator.ipynb` | Large-scale batch sweeps |

It also provides a CLI for automated parameter sweeps, making it a reference for how large-scale ML experiments can use NAIC infrastructure for both interactive and batch workflows.

## Quick Start

```bash
git clone https://github.com/NAICNO/wp7-UC1-climate-indices-teleconnection.git
cd wp7-UC1-climate-indices-teleconnection
bash setup.sh
jupyter notebook demonstrator-v1.orchestrator.ipynb
```

```{keypoints}
- Teleconnections are large-scale patterns of climate variability
- 65 climate indices from NorESM1-F simulations spanning 850–2005 AD
- ML ensemble of 5 model types identifies teleconnection relationships
- 42,613 experiments achieving >0.7 correlation for 20+ target indices
- Supports 10–50 year forecasts of AMV and PDV patterns
- Only WP7 demonstrator running on both NAIC Orchestrator and Sigma2 HPC
```
