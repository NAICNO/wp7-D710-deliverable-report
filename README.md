# D7.10 — Summary of Completed Demonstrators


**Deliverable D7.10** summarizes all seven NAIC Work Package 7 demonstrator projects, covering their scientific contributions, methodology, infrastructure requirements, and current status.

**Tutorial:** [https://naicno.github.io/wp7-D710-deliverable-report/](https://naicno.github.io/wp7-D710-deliverable-report/)

## Use Cases

| UC | Title | Repository | Tutorial | Status |
|----|-------|-----------|----------|--------|
| **UC1** | Climate Indices Teleconnection | [wp7-UC1-climate-indices-teleconnection](https://github.com/NAICNO/wp7-UC1-climate-indices-teleconnection) | [Tutorial](https://naicno.github.io/wp7-UC1-climate-indices-teleconnection/) | Completed |
| **UC2** | PEM Electrolyzer PINN Optimizer | [wp7-UC2-pem-electrolyzer-digital-twin](https://github.com/NAICNO/wp7-UC2-pem-electrolyzer-digital-twin) | [Tutorial](https://naicno.github.io/wp7-UC2-pem-electrolyzer-digital-twin/) | Completed |
| **UC3** | Pseudo-Hamiltonian Neural Networks | [wp7-UC3-pseudo-hamiltonian-neural-networks](https://github.com/NAICNO/wp7-UC3-pseudo-hamiltonian-neural-networks) | [Tutorial](https://naicno.github.io/wp7-UC3-pseudo-hamiltonian-neural-networks/) | Completed |
| **UC4** | 3D Medical Image Registration | [wp7-UC4-medical-image-registration](https://github.com/NAICNO/wp7-UC4-medical-image-registration) | [Tutorial](https://naicno.github.io/wp7-UC4-medical-image-registration/) | Completed |
| **UC5** | Graph-Based AIS Classification | [wp7-UC5-ais-classification-gnn](https://github.com/NAICNO/wp7-UC5-ais-classification-gnn) | [Tutorial](https://naicno.github.io/wp7-UC5-ais-classification-gnn/) | Completed |
| **UC6** | Multi-Modal Optimization | [wp7-UC6-multimodal-optimization](https://github.com/NAICNO/wp7-UC6-multimodal-optimization) | [Tutorial](https://naicno.github.io/wp7-UC6-multimodal-optimization/) | Completed |
| **UC7** | Latent Representation of PDE Solutions | [wp7-UC7-latent-pde-representation](https://github.com/NAICNO/wp7-UC7-latent-pde-representation) | [Tutorial](https://naicno.github.io/wp7-UC7-latent-pde-representation/) | Completed |

## Key Findings

- **Physics-informed ML generalizes better with fewer parameters** — UC2's 12-parameter student beats ~50K-parameter Transformers on out-of-distribution data by 5–6x
- **Data representation matters as much as model choice** — UC5's graph representation of vessel trajectories outperforms flat time series regardless of GNN architecture
- **NAIC infrastructure bridges interactive and batch computing** — UC1 runs on both Orchestrator VMs (interactive) and Sigma2 HPC (42,613 batch experiments)

## Repository Structure

```
D7.10-report.md          # Full deliverable report
content/                  # Sphinx-lesson tutorial documentation
  conf.py                 # Sphinx configuration
  index.rst               # Table of contents
  episodes/               # 12 tutorial episodes (UC1-UC7 + getting started + FAQ)
  images/                 # Logos and diagrams
  downloads/              # Quick reference page
tests/                    # 178 pytest tests (structure, report, episodes)
requirements-test.txt     # CI test dependencies
requirements-docs.txt     # Sphinx documentation dependencies
.gitlab-ci.yml            # CI/CD pipeline (test + GitLab Pages deploy)
```

## Documentation

The Sphinx-lesson tutorial covers:

1. **Getting Started** — Introduction, VM provisioning, quick start for any UC
2. **Use Cases** — Detailed walkthroughs for all 7 demonstrators (problem, approach, results, quick start)
3. **Cross-Cutting Themes** — Physics-informed ML, data representation, reproducibility, infrastructure patterns
4. **Reference** — FAQ, quick clone commands, useful links

## Running Tests

```bash
pip install -r requirements-test.txt
pytest tests/ -v
```

## Building Documentation Locally

```bash
pip install -r requirements-docs.txt
sphinx-build -b html content build/html
# Open build/html/index.html in your browser
```

## Contributors

| Institution | Contributors |
|-------------|-------------|
| NORCE Research | Klaus Johannsen, Adrian Evensen, Hasan Asyari Arief, Xue-Cheng Tai, Gro Fonnes, Yngve Heggelund |
| SINTEF Digital | Sølve Eidnes, Kjetil Olsen Lye |
| UiB | Saruar Alam |
| Sigma2 | Lorand Szentannai |

## License

- Content (tutorials, documentation): [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
- Code: [GPL-3.0-only](https://www.gnu.org/licenses/gpl-3.0.html)
