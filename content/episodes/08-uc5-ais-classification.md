# UC5 — Graph-Based Classification of AIS Time-Series Data

```{objectives}
- Understand how AIS vessel tracking data is structured
- Learn why graph representations outperform flat time series for vessel classification
- Compare three GNN architectures: GCN, GraphSAGE, GAT
- See how the framework supports both CPU and GPU training
```

**Repository:** [wp7-UC5-ais-classification-gnn](https://github.com/NAICNO/wp7-UC5-ais-classification-gnn)
**Contributors:** Xue-Cheng Tai, Gro Fonnes (NORCE Research)

## The Problem

Maritime surveillance generates large volumes of Automatic Identification System (AIS) data — position, speed, heading, and identity for thousands of vessels. A key task is **classifying vessel activities**, particularly distinguishing fishing from non-fishing behavior, which matters for:

- Fisheries management and quota enforcement
- Environmental monitoring
- Maritime safety

Traditional approaches use hand-crafted features and thresholds, but vessel movement patterns are complex and context-dependent.

## Key Insight: Graphs Instead of Sequences

Instead of treating AIS data as a flat time series, UC5 transforms each vessel's trajectory into a **graph structure**:

```{mermaid}
graph LR
    subgraph "Traditional Approach"
        A[t1] --> B[t2] --> C[t3] --> D[t4] --> E[t5]
    end
    subgraph "UC5 Graph Approach"
        F((t1)) --- G((t2))
        F --- H((t3))
        G --- H
        G --- I((t4))
        H --- I
        I --- J((t5))
    end
```

| Representation | Captures |
|---------------|----------|
| Flat time series | Temporal order only |
| Graph structure | Spatial + temporal relationships between trajectory points |

Nodes represent time steps. Edges encode spatial and temporal relationships between points. This richer representation captures patterns that flat sequences miss.

## GNN Architectures

Three graph neural network architectures were evaluated:

| Model | Architecture | Description |
|-------|-------------|-------------|
| **GCN** | Graph Convolutional Network | Spectral-based graph convolutions |
| **GraphSAGE (GSG)** | Sample and Aggregate | Inductive representation learning |
| **GAT** | Graph Attention Network | Attention-weighted neighbor aggregation |

All models are built on the **Deep Graph Library (DGL)** and support both CPU and GPU training with CUDA 11.8.

## Results

| Model | Test Accuracy |
|-------|--------------|
| GCN | 94.4% |
| **GraphSAGE** | **94.4%** |
| GAT | 93.1% |

**GraphSAGE achieved the best performance** at 94.4% test accuracy on fishing vs. non-fishing classification.

The key finding: representing AIS data as graphs instead of sequences mattered more than the choice of GNN architecture. The same idea applies to other domains with spatial-temporal data.

## Framework Features

| Feature | Details |
|---------|---------|
| Data pipeline | AIS CSV → graph construction → DGL dataset |
| Training | Configurable via YAML (model type, learning rate, epochs) |
| Evaluation | Accuracy, precision, recall, F1-score |
| GPU support | CUDA 11.8 with automatic fallback to CPU |
| Validation | Pydantic-based configuration validation |

## Quick Start

```bash
git clone https://github.com/NAICNO/wp7-UC5-ais-classification-gnn.git
cd graph-based-classification-of-ais-time-series-data
pip install -r requirements.txt
jupyter notebook demonstrator-v1.orchestrator.ipynb
```

```{keypoints}
- AIS data tracks vessel position, speed, heading, and identity
- Transforming trajectories into graphs captures spatial-temporal patterns flat time series miss
- Three GNN architectures evaluated: GCN, GraphSAGE, GAT
- GraphSAGE achieves 94.4% accuracy on fishing vs. non-fishing classification
- Data representation mattered more than model architecture choice
- Built on DGL with CPU and GPU (CUDA 11.8) support
```
