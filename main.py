import os
import argparse
import pandas as pd

from src.graph_reader import read_graph

from src.connected_components import (
    find_connected_components,
)

from src.scc import (
    find_strongly_connected_components,
)

from src.degree_distribution import (
    analyze_degree_distribution
)

from src.graph_visualizer import (
    visualize_graph
)

from src.graphlets import (
    analyze_graphlets
)

from src.orbits_counts import (
    analyze_graphlets_with_orbits
)

from src.centrality import (
    compute_centrality,
    top_k
)

from src.combined_visualization import (
    generate_combined_figure
)

from src.combined_graphlet_plot import (
    generate_combined_graphlet_figure
)

from src.combined_degree_distribution import (
    generate_combined_degree_distribution
)

def main():

    # ================= CLI =================
    parser = argparse.ArgumentParser(
        description="Graph Analysis Pipeline"
    )

    parser.add_argument(
        "--data_dir",
        type=str,
        default="data",
        help="Directory containing graph files"
    )

    args = parser.parse_args()

    data_dir = args.data_dir

    # ================= Validate =================
    if not os.path.exists(data_dir):
        print(f"ERROR: Directory not found -> {data_dir}")
        return

    graph_files = [
        os.path.join(data_dir, f)
        for f in os.listdir(data_dir)
        if f.endswith(".txt")
    ]

    if len(graph_files) == 0:
        print("No graph files found.")
        return

    os.makedirs("results", exist_ok=True)

    # ================= Storage =================
    summary_results = []

    graph_visualization_data = []

    graphlet_visualization_data = []
    
    degree_visualization_data = []

    # ================= Process Graphs =================
    for file_path in graph_files:

        print(f"\n{'='*70}")
        print(f"Processing: {file_path}")
        print(f"{'='*70}")

        graph_name = os.path.splitext(
            os.path.basename(file_path)
        )[0]

        # ================= Read Graph =================
        adj_undirected = read_graph(
            file_path,
            undirected=True
        )

        adj_directed = read_graph(
            file_path,
            undirected=False
        )

        num_nodes = len(adj_undirected)

        num_edges = (
            sum(
                len(neighbors)
                for neighbors in adj_undirected.values()
            ) // 2
        )
        
                # ================= Degree Data =================
        out_degrees = [
            len(adj_directed[node])
            for node in adj_directed
        ]

        # ---------- In-Degree ----------
        in_degree_map = {
            node: 0
            for node in adj_directed
        }

        for u in adj_directed:
            for v in adj_directed[u]:
                in_degree_map[v] += 1

        in_degrees = list(
            in_degree_map.values()
        )

        degree_visualization_data.append(
            (
                graph_name,
                out_degrees,
                in_degrees
            )
        )

        # ================= Components =================
        components = find_connected_components(
            adj_undirected
        )

        scc_list = find_strongly_connected_components(
            adj_directed
        )

        # ================= Density =================
        density = 0

        if num_nodes > 1:
            density = (
                2 * num_edges
            ) / (
                num_nodes * (num_nodes - 1)
            )

        # ================= Centrality =================
        degree_cent, betweenness_cent = (
            compute_centrality(adj_directed)
        )

        top_degree = top_k(degree_cent)

        top_between = top_k(betweenness_cent)

        # ================= Degree Plots =================
        analyze_degree_distribution(
            adj_directed,
            graph_name=graph_name
        )

        # ================= Visualization Data =================
        graph_visualization_data.append(
            (adj_directed, graph_name)
        )

        # ================= Graphlets =================
        graphlet_result = analyze_graphlets(
            file_path
        )

        graphlet_visualization_data.append(
            (graph_name, graphlet_result)
        )

        # ================= Orbit Analysis =================
        orbit_result = (
            analyze_graphlets_with_orbits(
                file_path
            )
        )

        # ================= Summary Table =================
        summary_results.append({

            "Graph": graph_name,

            "Nodes": num_nodes,

            "Edges": num_edges,

            "Density": round(density, 4),

            "Weakly Connected Components":
                len(components),

            "Strongly Connected Components":
                len(scc_list),

            "Triangles":
                graphlet_result.get(
                    "triangles",
                    0
                ),

            "3-Node Paths":
                graphlet_result.get(
                    "wedges",
                    0
                )
        })

    # ================= Save Summary Table =================
    df = pd.DataFrame(summary_results)

    summary_csv = (
        "results/summary_metrics.csv"
    )

    df.to_csv(
        summary_csv,
        index=False
    )

    print(f"\nSummary table saved: {summary_csv}")

    # ================= Combined Figures =================
    generate_combined_figure(
        graph_visualization_data
    )

    generate_combined_graphlet_figure(
        graphlet_visualization_data
    )

    generate_combined_degree_distribution(
        degree_visualization_data
    )


    print("\nAll analysis completed successfully!")


if __name__ == "__main__":
    main()