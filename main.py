import os
from src.graph_reader import read_graph
from src.connected_components import find_connected_components, print_components
from src.strongly_connected_components import find_strongly_connected_components, print_scc
from src.degree_distribution import analyze_degree_distribution   # ← Add this
from src.graph_visualizer import visualize_graph
from src.graphlet_counter import analyze_graphlets
from src.orbits_counts import analyze_graphlets_with_orbits
from src.generate_report import generate_report

def main():
    file_path = "data/graph5.txt"     # Change if needed
    print(f"Reading graph from: {file_path}")
    
    # 1. Read Graph (Undirected view for Weakly CC)
    adj_undirected = read_graph(file_path, undirected=True)
    
    edges_count = sum(len(neighbors) for neighbors in adj_undirected.values()) // 2
    print(f"Nodes: {len(adj_undirected)}")
    print(f"Edges: {edges_count}")
    
    # 2. Connected Components (Weakly)
    components = find_connected_components(adj_undirected)
    print_components(components)
    
    # 3. Strongly Connected Components (Directed)
    print("\n=== Analyzing Directed Graph ===")
    adj_directed = read_graph(file_path, undirected=False)
    scc_list = find_strongly_connected_components(adj_directed)
    print_scc(scc_list)
    
    # 4. Degree Distribution + Auto Save Plot  ←←← THIS WAS MISSING
    print("\n=== Degree Distribution Analysis ===")
    degree_plot_path = analyze_degree_distribution(adj_directed, graph_name=file_path)

    print("\n=== Generating Graph Visualization ===")
    visualization_path = visualize_graph(
        adj_directed,
        file_path=file_path,
        title="Directed Graph Visualization"
    )

    print("\n=== 3-Node Graphlet Analysis ===")
    graphlet_result = analyze_graphlets(file_path)
    
    # 6. 3-Node Graphlet Orbits (GRAAL style)
    print("\n=== 3-Node Graphlet Orbit Analysis ===")
    orbit_result = analyze_graphlets_with_orbits(file_path)
    
    # ====================== Generate Report ======================
    print("\n=== Generating Full Report ===")
    
    graph_name = os.path.splitext(os.path.basename(file_path))[0]
    report_path = f"results/{graph_name}_FULL_REPORT.txt"
    
    generate_report(
        output_file=report_path,
        file_path=file_path,
        num_nodes=len(adj_undirected),
        num_edges=edges_count,
        weak_components=components,
        scc_list=scc_list,
        graphlet_result=graphlet_result,
        orbit_counts=orbit_result,                    # ← Orbits added
        degree_plot_path=degree_plot_path,
        visualization_path=visualization_path
    )

    print("\n🎉 All analysis completed successfully!")


if __name__ == "__main__":
    main()