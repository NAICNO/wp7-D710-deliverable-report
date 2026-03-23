"""
Pytest fixtures and constants shared across the D7.10 test suite.
"""

import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORT_PATH = os.path.join(PROJECT_ROOT, "D7.10-report.md")
README_PATH = os.path.join(PROJECT_ROOT, "README.md")
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")
EPISODES_DIR = os.path.join(CONTENT_DIR, "episodes")

# All seven use cases referenced in the report
USE_CASES = [
    {"id": "UC1", "title": "Climate Indices Teleconnection", "repo": "wp7-UC1-climate-indices-teleconnection"},
    {"id": "UC2", "title": "PEM Electrolyzer PINN Optimizer", "repo": "wp7-UC2-pem-electrolyzer-digital-twin"},
    {"id": "UC3", "title": "Pseudo-Hamiltonian Neural Networks", "repo": "wp7-UC3-pseudo-hamiltonian-neural-networks"},
    {"id": "UC4", "title": "3D Medical Image Registration", "repo": "wp7-UC4-medical-image-registration"},
    {"id": "UC5", "title": "Graph-Based Classification of AIS", "repo": "wp7-UC5-ais-classification-gnn"},
    {"id": "UC6", "title": "Multi-Modal Optimization", "repo": "wp7-UC6-multimodal-optimization"},
    {"id": "UC7", "title": "Latent Representation of PDE Solutions", "repo": "wp7-UC7-latent-pde-representation"},
]

UC_IDS = [uc["id"] for uc in USE_CASES]

# Expected episode files
EPISODE_FILES = [
    "01-introduction.md",
    "02-provision-vm.md",
    "03-getting-started.md",
    "04-uc1-climate-teleconnection.md",
    "05-uc2-pem-electrolyzer.md",
    "06-uc3-pseudo-hamiltonian.md",
    "07-uc4-medical-imaging.md",
    "08-uc5-ais-classification.md",
    "09-uc6-multimodal-optimization.md",
    "10-uc7-latent-pde.md",
    "11-common-patterns.md",
    "12-faq.md",
]
