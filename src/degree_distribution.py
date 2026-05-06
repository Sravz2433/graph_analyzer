import os
from collections import defaultdict
from typing import Dict, Set, Tuple
import matplotlib.pyplot as plt

def ensure_results_folder():
    """Create results folder if it doesn't exist"""
    if not os.path.exists('results'):
        os.makedirs('results')
        print("📁 Created 'results' folder")


def compute_degrees(adj: Dict[int, Set[int]]) -> Tuple[Dict[int, int], Dict[int, int]]:
    out_degree = defaultdict(int)
    in_degree = defaultdict(int)

    for node in adj:
        out_degree[node] = 0
        in_degree[node] = 0

    for u in adj:
        out_degree[u] = len(adj[u])
        for v in adj[u]:
            in_degree[v] += 1

    return dict(out_degree), dict(in_degree)


def degree_distribution(degrees: Dict[int, int]) -> Dict[int, int]:
    dist = defaultdict(int)
    for deg in degrees.values():
        dist[deg] += 1
    return dict(dist)


def print_degree_stats(out_degree: Dict[int, int], in_degree: Dict[int, int]):
    out_values = list(out_degree.values())
    in_values = list(in_degree.values())

    print("\n=== Degree Statistics ===")
    print(f"Max Out-Degree : {max(out_values)}")
    print(f"Min Out-Degree : {min(out_values)}")
    print(f"Avg Out-Degree : {sum(out_values)/len(out_values):.3f}")
    print(f"Max In-Degree  : {max(in_values)}")
    print(f"Min In-Degree  : {min(in_values)}")
    print(f"Avg In-Degree  : {sum(in_values)/len(in_values):.3f}")


def plot_and_save_degree_distribution(out_dist: Dict[int, int], 
                                      in_dist: Dict[int, int], 
                                      graph_name: str = "graph"):
    """Plot and automatically save the degree distribution"""
    ensure_results_folder()
    
    plt.figure(figsize=(12, 5))

    # Out-degree
    plt.subplot(1, 2, 1)
    plt.bar(out_dist.keys(), out_dist.values(), color='skyblue', edgecolor='black')
    plt.title("Out-Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Number of Nodes")
    plt.grid(True, alpha=0.3)

    # In-degree
    plt.subplot(1, 2, 2)
    plt.bar(in_dist.keys(), in_dist.values(), color='lightcoral', edgecolor='black')
    plt.title("In-Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Number of Nodes")
    plt.grid(True, alpha=0.3)

    safe_name = os.path.splitext(os.path.basename(graph_name))[0]
    plt.suptitle(f"Degree Distribution - {safe_name}")
    plt.tight_layout()

    # Save plot
    save_path = f"results/{safe_name}_degree_distribution.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"📊 Plot saved: {save_path}")
    
    plt.close()  # Close plot to free memory


def analyze_degree_distribution(adj: Dict[int, Set[int]], graph_name: str = "graph"):
    """Main function - Compute, Print & Save"""
    out_degree, in_degree = compute_degrees(adj)
    
    print_degree_stats(out_degree, in_degree)
    
    out_dist = degree_distribution(out_degree)
    in_dist = degree_distribution(in_degree)
    
    print("\nOut-Degree Distribution:")
    for deg in sorted(out_dist.keys()):
        print(f"  Degree {deg:2d} : {out_dist[deg]:3d} nodes")
    
    # Plot and auto-save
    plot_and_save_degree_distribution(out_dist, in_dist, graph_name)