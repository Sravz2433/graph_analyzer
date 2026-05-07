from typing import Dict, Set
from src.graph_reader import read_graph

def count_3_node_graphlets(adj: Dict[int, Set[int]], undirected: bool = True):
    triangles = 0
    wedges = 0

    for v in adj:
        deg = len(adj[v])
        if deg >= 2:
            wedges += deg * (deg - 1) // 2

    for u in adj:
        for v in adj[u]:
            if undirected and v <= u:
                continue
            common = len(adj[u] & adj[v])
            triangles += common

    if undirected:
        triangles //= 3
        wedges -= 3 * triangles

    total = triangles + wedges

    return {
        "triangles": triangles,
        "wedges": wedges,
        "total_3_graphlets": total
    }


def analyze_graphlets(file_path: str):
    print(f"\n=== 3-Node Graphlet Analysis for {file_path} ===")

    adj = read_graph(file_path, undirected=True)
    stats = count_3_node_graphlets(adj, undirected=True)

    print(f"  Triangles : {stats['triangles']}")
    print(f"  Wedges    : {stats['wedges']}")
    print(f"  Total 3-node graphlets : {stats['total_3_graphlets']}")

    return stats