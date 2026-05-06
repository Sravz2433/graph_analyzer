def generate_report(
    output_file,
    file_path,
    num_nodes,
    num_edges,
    weak_components,
    scc_list,
    graphlet_result=None,
    orbit_counts=None,          # ← New: Added for orbits
    degree_plot_path=None,
    visualization_path=None
):
    """
    Generate comprehensive analysis report including 3-node graphlet orbits
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("GRAPH ANALYSIS REPORT\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"Source File: {file_path}\n")
        f.write(f"Nodes: {num_nodes}\n")
        f.write(f"Edges: {num_edges}\n\n")

        # Weakly Connected Components
        f.write("WEAKLY CONNECTED COMPONENTS\n")
        f.write("-" * 70 + "\n")
        f.write(f"Total Components: {len(weak_components)}\n")
        for i, comp in enumerate(weak_components, 1):
            f.write(f"Component {i}: Size = {len(comp)}, Nodes = {sorted(comp)}\n")
        f.write("\n")

        # Strongly Connected Components
        f.write("STRONGLY CONNECTED COMPONENTS\n")
        f.write("-" * 70 + "\n")
        f.write(f"Total SCCs: {len(scc_list)}\n")
        for i, comp in enumerate(scc_list, 1):
            f.write(f"SCC {i}: Size = {len(comp)}, Nodes = {sorted(comp)}\n")
        f.write("\n")

        # 3-Node Graphlets + Orbits
        if graphlet_result is not None or orbit_counts is not None:
            f.write("3-NODE GRAPHLET ANALYSIS (GRAAL Style)\n")
            f.write("-" * 70 + "\n")
            
            if graphlet_result is not None:
                f.write(f"3-node Paths (Wedges) : {graphlet_result.get('wedges', 0)}\n")
                f.write(f"Triangles            : {graphlet_result.get('triangles', 0)}\n")
                f.write(f"Total 3-Graphlets    : {graphlet_result.get('total_3_graphlets', 0)}\n\n")

            if orbit_counts is not None:
                # Calculate totals
                total_orbit0 = sum(oc[0] for oc in orbit_counts.values())
                total_orbit1 = sum(oc[1] for oc in orbit_counts.values())
                total_orbit2 = sum(oc[2] for oc in orbit_counts.values())

                f.write("ORBIT COUNTS (3-Node Graphlets):\n")
                f.write(f"  Orbit 0 - Wedge Endpoints     : {total_orbit0}\n")
                f.write(f"  Orbit 1 - Wedge Centers       : {total_orbit1}\n")
                f.write(f"  Orbit 2 - Triangle Nodes      : {total_orbit2}\n")
                f.write(f"  Total Orbit Instances         : {total_orbit0 + total_orbit1 + total_orbit2}\n")
            f.write("\n")

        # Degree Plot
        if degree_plot_path:
            f.write("DEGREE DISTRIBUTION PLOT\n")
            f.write("-" * 70 + "\n")
            f.write(f"Saved Plot: {degree_plot_path}\n\n")

        # Graph Visualization
        if visualization_path:
            f.write("GRAPH VISUALIZATION\n")
            f.write("-" * 70 + "\n")
            f.write(f"Saved Visualization: {visualization_path}\n\n")

        f.write("=" * 70 + "\n")
        f.write("Report generated successfully.\n")

    print(f"📋 Report saved to: {output_file}")