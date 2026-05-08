import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Set


def visualize_graph(
    adj: Dict[int, Set[int]],
    ax,
    graph_name: str,
    title: str = "Graph Visualization",
    node_size: int = 300,
    arrow_size: int = 10
):
    """
    Draw graph on matplotlib subplot axis
    """

    # ================= Create Graph =================
    G = nx.DiGraph()

    for u in adj:
        G.add_node(u)

        for v in adj[u]:
            G.add_edge(u, v)

    # ================= Layout =================
    pos = nx.spring_layout(
        G,
        seed=42,
        k=0.5
    )

    # ================= Draw =================
    nx.draw(
        G,
        pos,
        ax=ax,
        with_labels=True,
        node_color="lightblue",
        node_size=node_size,
        font_size=5,
        edge_color="gray",
        arrows=True,
        arrowsize=arrow_size,
        alpha=0.9
    )

    ax.set_title(
        f"{graph_name}\n"
        f"{len(G.nodes)} nodes, {len(G.edges)} edges",
        fontsize=10
    )

    ax.axis("off")