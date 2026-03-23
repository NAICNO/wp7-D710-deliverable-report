# FAQ

```{objectives}
- Find answers to common questions about WP7 demonstrators
- Troubleshoot common setup and runtime issues
- Understand licensing, contributions, and future work
```

## General

### Which use case should I start with?

It depends on your background:

| Background | Recommended Starting Point |
|-----------|---------------------------|
| Climate science | UC1 — Climate Teleconnection Analysis |
| Energy / green hydrogen | UC2 — PEM Electrolyzer PINN Optimizer |
| Physics / dynamical systems | UC3 — Pseudo-Hamiltonian Neural Networks |
| Medical imaging | UC4 — 3D Medical Image Registration |
| Maritime / geospatial | UC5 — Graph-Based AIS Classification |
| Optimization / operations research | UC6 — Multi-Modal Optimization |
| Scientific computing / PDEs | UC7 — Latent PDE Representations |

If you want the most polished experience, start with **UC1**, **UC2**, or **UC6** — these have the most detailed multi-chapter tutorials (8–10 episodes each).

### Do I need a GPU?

Not always:

| UC | GPU Required? |
|----|--------------|
| UC1 | No (CPU sufficient for all models) |
| UC2 | Recommended (faster training) |
| UC3 | Recommended |
| UC4 | No (CPU sufficient) |
| UC5 | Recommended (CUDA 11.8) |
| UC6 | No (CPU, but multi-core parallelization helps) |
| UC7 | Recommended |

### Can I run these on my laptop?

Yes, for smaller-scale experiments. The notebooks are designed to run on NAIC Orchestrator VMs for full-scale training, but most include options for reduced parameter sweeps or smaller datasets that work on a laptop.

### How do I use an AI coding assistant?

Six repositories (UC1, UC2, UC3, UC5, UC6, UC7) include `AGENT.md` files. Tell your assistant:

> "Read AGENT.md and help me run the demonstrator."

The assistant will set up the environment and run experiments automatically.

## Infrastructure

### How do I get access to NAIC Orchestrator?

1. Register with [MyAccessID](https://puhuri.neic.no/user_guides/myaccessid_registration/) using your Feide account
2. Login to [orchestrator.naic.no](https://orchestrator.naic.no/)
3. Create a VM (see [Episode 02](02-provision-vm.md))

If your institute is not registered, contact support@naic.no.

### My SSH connection is refused — what do I do?

Check these common causes:
1. **IP changed**: If you switched networks (home/office/VPN), add your new IP in the Orchestrator
2. **Key permissions**: Ensure `chmod 600 your-key.pem` (Linux/Mac) or restrict via icacls (Windows)
3. **VM expired**: VMs are short-lived — check if your duration has expired

### How do I access Jupyter on the VM?

Create an SSH tunnel:

```bash
ssh -i /path/to/key.pem -L 8888:localhost:8888 ubuntu@<VM_IP>
```

Then open `http://localhost:8888` in your browser.

## Technical

### Why do some tests skip in CI?

Tests are designed to skip gracefully when optional heavy dependencies are unavailable:
- `dgl` (UC5) — requires CUDA and C++ graphbolt library
- `torch` (UC2, UC3) — installed separately with CPU-only wheels in CI
- `requests`, `fastapi` (UC2) — only needed for digital twin smoke tests
- `antspyx`, `hd-bet` (UC4) — heavy medical imaging dependencies

This ensures CI pipelines pass quickly while still validating project structure and code logic.

### What Python version is required?

All repositories target **Python 3.11**. CI pipelines use the `python:3.11-slim` Docker image. UC4 uses Conda with Python 3.11 pinned in `environment.yml`.

### How are the repositories licensed?

Most repositories use dual licensing:
- **CC BY-NC 4.0** for content (tutorials, documentation, notebooks)
- **GPL-3.0-only** for code

UC7 currently uses MIT; this will be updated for consistency.

## Contributing

### How can I contribute to a use case?

1. Fork the repository on GitLab Sigma2
2. Create a feature branch
3. Follow the existing code style and test patterns
4. Submit a merge request

### Who do I contact for questions?

| UC | Contact |
|----|---------|
| UC1 | Klaus Johannsen (NORCE) |
| UC2 | Hasan Asyari Arief (NORCE) |
| UC3 | Sølve Eidnes (SINTEF) |
| UC4 | Saruar Alam (UiB) |
| UC5 | Xue-Cheng Tai (NORCE) |
| UC6 | Klaus Johannsen (NORCE) |
| UC7 | Klaus Johannsen (NORCE) |

For infrastructure issues: support@naic.no

```{keypoints}
- Start with UC1, UC2, or UC6 for the most detailed tutorials (8–10 episodes)
- GPU is recommended but not required for most use cases
- AGENT.md files enable AI coding assistants to set up and run demonstrators
- Tests skip gracefully when heavy dependencies are unavailable
- All repos target Python 3.11 with lean CI pipelines
```
