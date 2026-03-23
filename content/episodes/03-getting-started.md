# Getting Started with Any Use Case

```{objectives}
- Clone and set up any WP7 demonstrator repository
- Understand the common repository layout
- Run the demonstrator notebook end-to-end
- Use AI coding assistants with AGENT.md files
```

## Common Repository Layout

Every completed WP7 demonstrator follows a consistent layout:

```
<repo-root>/
├── README.md                           # Project overview
├── requirements.txt                    # Python dependencies (full VM)
├── requirements-test.txt               # Lean CI dependencies
├── setup.sh or vm-init.sh              # One-command setup script
├── demonstrator-v1.orchestrator.ipynb  # Interactive notebook
├── dataset/ or data/                   # Training data (included or downloaded)
├── scripts/ or src/                    # Source code
├── results/                            # Pre-computed results (optional)
├── tests/                              # Automated test suite
├── content/                            # Sphinx tutorial (all repos)
├── AGENT.md                            # AI assistant instructions (all except UC4)
└── .gitlab-ci.yml                      # CI/CD pipeline
```

## Quick Start (Any Use Case)

Once connected to your NAIC VM (see [Episode 02](02-provision-vm.md)):

### 1. Clone the repository

```bash
# Replace <REPO_NAME> with the actual repository name
git clone https://github.com/NAICNO/<REPO_NAME>.git
cd <REPO_NAME>
```

### 2. Set up the environment

````{tabs}
```{tab} Using setup.sh (all except UC4)
# One-command setup
bash setup.sh
```

```{tab} Using requirements.txt
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```{tab} Using Conda (UC4)
conda env create -f environment.yml
conda activate 3d-image-registration-segmentation
```
````

### 3. Launch Jupyter

```bash
# Start Jupyter in the background
jupyter notebook --no-browser --port=8888 &
```

On your local machine, create an SSH tunnel:

```bash
ssh -i /path/to/key.pem -L 8888:localhost:8888 ubuntu@<VM_IP>
```

Then open `http://localhost:8888` in your browser.

### 4. Run the notebook

Open `demonstrator-v1.orchestrator.ipynb` (or the use case's main notebook) and run all cells.

## Use Case Quick Reference

| UC | Repository | Clone Command |
|----|-----------|---------------|
| UC1 | d7.2-Use-case1 | `git clone https://github.com/NAICNO/wp7-UC1-climate-indices-teleconnection.git` |
| UC2 | uc2-pem-electrolyzer-pinn-optimizer | `git clone https://github.com/NAICNO/wp7-UC2-pem-electrolyzer-digital-twin.git` |
| UC3 | pseudo-hamiltonian-neural-networks | `git clone https://github.com/NAICNO/wp7-UC3-pseudo-hamiltonian-neural-networks.git` |
| UC4 | 3D-medical-image-registration-segmentation | `git clone https://github.com/NAICNO/wp7-UC4-medical-image-registration.git` |
| UC5 | graph-based-classification-of-ais-time-series-data | `git clone https://github.com/NAICNO/wp7-UC5-ais-classification-gnn.git` |
| UC6 | multi-modal-optimization | `git clone https://github.com/NAICNO/wp7-UC6-multimodal-optimization.git` |
| UC7 | latent-representation-of-pde-solutions | `git clone https://github.com/NAICNO/wp7-UC7-latent-pde-representation.git` |

## Using AI Coding Assistants

Six repositories (UC1, UC2, UC3, UC5, UC6, UC7) include `AGENT.md` files with machine-readable instructions for AI coding assistants like **Claude Code**, **GitHub Copilot**, or **Cursor**.

To use this:

```
> "Read AGENT.md and help me run the demonstrator on my NAIC VM."
```

The assistant will be able to set up the environment and run experiments automatically.

## GPU Requirements

| UC | GPU Required? | Typical Training Time |
|----|--------------|----------------------|
| UC1 | No (CPU sufficient) | 5–30 min per model |
| UC2 | Recommended | ~10 min (teacher + student) |
| UC3 | Recommended | Varies by system |
| UC4 | No (CPU sufficient) | ~5 min per subject |
| UC5 | Recommended (CUDA 11.8) | ~15 min training |
| UC6 | No (CPU, multi-core helps) | ~5 min per function |
| UC7 | Recommended | ~20 min (autoencoder training) |

## Running Tests

Every repository includes a test suite that runs without GPU or heavy dependencies:

```bash
pip install -r requirements-test.txt
pytest tests/ -v --tb=short
```

Tests are designed to skip gracefully when optional dependencies (e.g., DGL, TensorFlow, requests) are not installed.

```{keypoints}
- All WP7 repositories follow a consistent layout: notebook + data + setup script + tests
- One-command setup scripts (`setup.sh`, `vm-init.sh`) handle environment creation
- SSH tunneling provides Jupyter access from your local browser
- AI coding assistants can use AGENT.md files for automated setup (all except UC4)
- Tests skip gracefully in CI environments without GPU or heavy dependencies
```
