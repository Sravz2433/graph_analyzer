import os
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Set

def ensure_results_folder():
    if not os.path.exists('results'):
        os.makedirs('results')

def visualize_graph(adj: Dict[int, Set[int]], 
                   file_path: str, 
                   title: str = "Graph Visualization",
                   node_size: int = 500,
                   arrow_size: int = 12):
    """
    Visualize the graph and save it as PNG
    """
    ensure_results_folder()
    
    # Create NetworkX graph
    G = nx.DiGraph() if any(adj[u] for u in adj) else nx.Graph()
    
    for u in adj:
        G.add_node(u)
        for v in adj[u]:
            G.add_edge(u, v)
    
    graph_name = os.path.splitext(os.path.basename(file_path))[0]
    save_path = f"results/{graph_name}_visualization.png"
    
    plt.figure(figsize=(14, 10))
    
    # Use spring layout for better visualization
    pos = nx.spring_layout(G, seed=42, k=0.5)
    
    # Draw the graph
    nx.draw(G, pos, 
            with_labels=True,
            node_color='lightblue',
            node_size=node_size,
            font_size=8,
            font_weight='bold',
            edge_color='gray',
            arrows=True,
            arrowsize=arrow_size,
            alpha=0.9)
    
    plt.title(f"{title}\n{graph_name} - {len(G.nodes)} nodes, {len(G.edges)} edges", 
              fontsize=14, pad=20)
    
    # Save high quality image
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"🖼️ Graph visualization saved: {save_path}")
    
    plt.close()
    return save_path