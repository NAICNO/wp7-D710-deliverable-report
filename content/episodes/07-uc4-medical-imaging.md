# UC4 — 3D Medical Image Registration & Segmentation

```{objectives}
- Understand why multi-modal MRI registration matters for brain tumor diagnosis
- Learn about the registration pipeline: N4 bias correction, HD-BET, ANTsPy
- Know the four MRI modalities and their clinical roles
- Understand the SRI-24 atlas alignment workflow
```

**Repository:** [wp7-UC4-medical-image-registration](https://github.com/NAICNO/wp7-UC4-medical-image-registration)
**Contributors:** Saruar Alam (UiB)

## The Problem

Brain tumor diagnosis and monitoring rely on multiple MRI modalities, each highlighting different tissue characteristics. Before these modalities can be analyzed together — to delineate tumor boundaries or estimate tumor volume — the images must be **spatially aligned**.

This registration step is critical for both clinical practice and automated segmentation research.

## MRI Modalities

Each modality contributes a different clinical perspective:

| Modality | Full Name | Clinical Role |
|----------|-----------|---------------|
| **T1** | T1-weighted | Detailed anatomical structure |
| **T1Gd** | T1 with gadolinium contrast | Highlights active tumor tissue (enhancing regions) |
| **T2** | T2-weighted | Sensitive to fluids, revealing edema and infiltration |
| **FLAIR** | Fluid-Attenuated Inversion Recovery | Differentiates CSF from lesions, especially near ventricles |

## Registration Pipeline

The pipeline combines two established medical imaging tools:

```{mermaid}
graph TD
    A[Raw MRI Scans<br>T1, T1Gd, T2, FLAIR] --> B[N4 Bias Correction<br>Remove intensity non-uniformities]
    B --> C[HD-BET Brain Extraction<br>AI-based skull stripping]
    C --> D[Rigid Registration<br>All modalities → T1Gd reference]
    D --> E[Atlas Registration<br>T1Gd → SRI-24 standard atlas]
    E --> F[Propagate Transforms<br>Apply to all modalities]
    F --> G[Aligned Multi-Modal Volumes<br>Ready for segmentation]
```

### Step-by-step:

1. **N4 Bias Correction** — Removes intensity non-uniformities caused by magnetic field inhomogeneities
2. **HD-BET Brain Extraction** — AI-based skull stripping to isolate brain tissue
3. **Rigid Registration** — Aligns all modalities to the T1Gd reference using ANTsPy
4. **Atlas Registration** — Registers T1Gd to the SRI-24 standard brain atlas
5. **Transform Propagation** — Applies all computed transformations to the remaining modalities

### Tools Used

| Tool | Purpose |
|------|---------|
| **HD-BET** | High-Definition Brain Extraction Tool — AI-based skull stripping |
| **ANTsPy** | Advanced Normalization Tools for Python — registration and transformation |
| **nibabel** | NIfTI image I/O |
| **SRI-24 Atlas** | Standard brain atlas for spatial normalization |

## Data: BraTS Dataset

The pipeline is designed for the Brain Tumor Segmentation (BraTS) challenge dataset:
- Multi-institutional MRI scans
- Expert-annotated tumor boundaries
- Multiple modalities per subject

## Environment Setup

UC4 uses a Conda environment for reproducibility:

```bash
git clone https://github.com/NAICNO/wp7-UC4-medical-image-registration.git
cd 3D-medical-image-registration-segmentation
conda env create -f environment.yml
conda activate 3d-image-registration-segmentation
```

Key dependencies: `antspyx`, `nibabel`, `numpy`, `scipy`, `hd-bet`

## Status

UC4 provides the core registration pipeline with a Conda environment, an orchestrator notebook with synthetic 3D data for demonstration, a full test suite, and CI/CD pipeline. UC4 is the only WP7 use case in **healthcare**, where reproducible computational pipelines are especially important for clinical research.

```{keypoints}
- Brain tumor diagnosis requires spatial alignment of multiple MRI modalities
- Four MRI modalities (T1, T1Gd, T2, FLAIR) each reveal different tissue characteristics
- HD-BET provides AI-based brain extraction; ANTsPy handles registration
- Pipeline: N4 bias correction → brain extraction → rigid alignment → atlas registration
- SRI-24 atlas enables standardized spatial normalization across subjects
- Only WP7 use case in the healthcare domain
```
