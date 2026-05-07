# Graph Analysis and Biological Network Characterization

This project implements a graph analysis pipeline for studying network topology, connectivity, and local structural motifs in biological-style networks. The work was developed as part of the graph theory and biological network alignment research challenge proposed by Prof. Wayne B. Hayes (UC Irvine).

The project focuses on:

* Connected component analysis
* Strongly connected component (SCC) detection
* Degree distribution analysis
* Graph density estimation
* Centrality analysis
* 3-node graphlet characterization
* Graph visualization and reporting

In addition to the required challenge tasks, the project incorporates concepts from the GRAAL (GRAph ALigner) framework for topology-based biological network alignment.

---

# Biological Motivation

Biological systems such as:

* protein–protein interaction (PPI) networks
* gene regulatory networks
* metabolic pathways

can be represented as graphs, where nodes represent biological entities and edges represent interactions or relationships.

Analyzing graph topology helps identify:

* hub nodes
* modular structures
* interaction motifs
* local connectivity patterns
* functionally important subnetworks

This project explores these concepts through graph-theoretic analysis and graphlet-based characterization.

---

# Features

## Core Graph Analysis

* Graph parsing from edge-list text files
* Weakly connected component detection
* Strongly connected component (SCC) computation
* Duplicate edge handling
* Sparse and dense graph support

## Degree Analysis

* Degree computation
* In-degree and out-degree analysis
* Degree distribution histograms

## Graphlet Analysis

Implementation of connected 3-node graphlets:

* Triangles
* 3-node paths (wedges)

Inspired by:

* GRAAL (Graph Aligner)
* topology-aware biological network analysis

## Network Metrics

* Graph density
* Degree centrality
* Betweenness centrality

## Visualization

* Graph visualization
* Histogram plotting
* Automated report generation

---

# Project Structure

```text
graph-network-analysis/
│
├── data/
│   ├── graph1.txt
│   ├── graph2.txt
│   └── ...
│
├── results/
│   ├── reports/
│   ├── plots/
│   ├── visualizations/
│   └── ...
│
├── src/
│   ├── graph_reader.py
│   ├── connected_components.py
│   ├── scc.py
│   ├── graphlets.py
│   ├── centrality.py
│   ├── visualization.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Input Format

Each graph file follows this format:

```text
N
u1 v1
u2 v2
u3 v3
...
```

Where:

* `N` = number of nodes
* Remaining lines represent edges

Example:

```text
5
0 1
1 2
2 3
3 4
```

---

# Algorithms Used

## Connected Components

* Breadth-First Search (BFS)
  or
* Depth-First Search (DFS)

## Strongly Connected Components

* Kosaraju's Algorithm

## Graphlet Counting

Efficient combinatorial counting for:

* triangles
* open wedges / 3-node paths

## Centrality Measures

* Degree Centrality
* Betweenness Centrality

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd graph-network-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the analysis pipeline:

```bash
python main.py
```

Outputs will be generated in the `results/` directory.

---

# Example Outputs

Generated outputs include:

* Graph analysis reports
* Degree histograms
* In-degree / out-degree distributions
* Graph visualizations
* Graphlet statistics

---

# Graphlet Interpretation

3-node graphlets capture local topological organization within networks.

## Triangles

Triangles often indicate:

* densely interacting modules
* cooperative interactions
* clustered subnetworks

## 3-Node Paths

3-node paths may represent:

* interaction bridges
* sparse communication structures
* local connectivity chains

Graphlet-based representations are widely used in:

* biological network alignment
* systems biology
* protein interaction analysis
* network topology characterization

---

# References

1. Kuchaiev O., Milenković T., Memišević V., Hayes W., Pržulj N.
   *Topological network alignment uncovers biological function and phylogeny.*
   Journal of the Royal Society Interface, 2010.

2. Pržulj N.
   *Biological network comparison using graphlet degree distribution.*
   Bioinformatics, 2007.

3. Singh R. et al.
   *Pairwise global alignment of protein interaction networks by matching neighborhood topology.*
   RECOMB, 2007.

---

# Author

Sravya Sri Mallampalli
B.Tech Computer Science and Engineering
Indian Institute of Information Technology, Sri City

Research Interests:

* Computational Biology
* Network Biology
* Multimodal Omics
* Graph Machine Learning
* Systems Biology
