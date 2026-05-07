import os
import argparse

from src.graph_reader import read_graph
from src.connected_components import (
    find_connected_components,
    print_components
)
from src.scc import (
    find_strongly_connected_components,
    print_scc
)
from src.degree_distribution import analyze_degree_distribution
from src.graph_visualizer import visualize_graph
from src.graphlets import analyze_graphlets
from src.orbits_counts import analyze_graphlets_with_orbits
from src.report_generator import generate_report


def main():

    # ================= CLI Argument Parsing =================
    parser = argparse.ArgumentParser(
        description="Graph Analysis and Biological Network Characterization"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to graph input file"
    )

    args = parser.parse_args()

    file_path = args.input

    # ================= Validate Input =================
    if not os.path.exists(file_path):
        print(f"ERROR: File not found -> {file_path}")
        return

    print(f"\nReading graph from: {file_path}")

    # ================= Read Undirected Graph =================
    adj_undirected = read_graph(file_path, undirected=True)

    edges_count = (
        sum(len(neighbors) for neighbors in adj_undirected.values()) // 2
    )

    print(f"Nodes: {len(adj_undirected)}")
    print(f"Edges: {edges_count}")

    # ================= Connected Components =================
    print("\n=== Weakly Connected Components ===")

    components = find_connected_components(adj_undirected)

    print_components(components)

    # ================= Directed Graph =================
    print("\n=== Strongly Connected Components ===")

    adj_directed = read_graph(file_path, undirected=False)

    scc_list = find_strongly_connected_components(adj_directed)

    print_scc(scc_list)

    # ================= Degree Distribution =================
    print("\n=== Degree Distribution Analysis ===")

    degree_plot_path = analyze_degree_distribution(
        adj_directed,
        graph_name=file_path
    )

    # ================= Graph Visualization =================
    print("\n=== Generating Graph Visualization ===")

    visualization_path = visualize_graph(
        adj_directed,
        file_path=file_path,
        title="Directed Graph Visualization"
    )

    # ================= Graphlet Analysis =================
    print("\n=== 3-Node Graphlet Analysis ===")

    graphlet_result = analyze_graphlets(file_path)

    # ================= Orbit Analysis =================
    print("\n=== 3-Node Graphlet Orbit Analysis ===")

    orbit_result = analyze_graphlets_with_orbits(file_path)

    # ================= Report Generation =================
    print("\n=== Generating Full Report ===")

    os.makedirs("results", exist_ok=True)

    graph_name = os.path.splitext(
        os.path.basename(file_path)
    )[0]

    report_path = f"results/{graph_name}_FULL_REPORT.txt"

    generate_report(
        output_file=report_path,
        file_path=file_path,
        num_nodes=len(adj_undirected),
        num_edges=edges_count,
        weak_components=components,
        scc_list=scc_list,
        graphlet_result=graphlet_result,
        orbit_counts=orbit_result,
        degree_plot_path=degree_plot_path,
        visualization_path=visualization_path
    )

    print("\nAll analysis completed successfully!")


if __name__ == "__main__":
    main()