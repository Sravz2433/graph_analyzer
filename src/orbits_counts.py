from collections import defaultdict
import os
from typing import Dict, List, Tuple
from src.graph_reader import read_graph

def count_3_node_orbits(adj: Dict[int, set]) -> Dict[int, List[int]]:
    """
    Returns orbit counts for each node.
    Orbits for 3-node graphlets:
        Orbit 0 : End node of a wedge (2-path)
        Orbit 1 : Middle node of a wedge (2-path)
        Orbit 2 : Node in a triangle
    """
    orbit_count = defaultdict(lambda: [0, 0, 0])  # [orbit0, orbit1, orbit2]

    for u in adj:
        neighbors_u = list(adj[u])
        deg_u = len(neighbors_u)
        
        for i in range(deg_u):
            v = neighbors_u[i]
            if v < u: 
                continue  # Avoid double counting edges
                
            common_neighbors = 0
            for w in adj[v]:
                if w != u and w in adj[u]:
                    common_neighbors += 1
                    
                    # Triangle: u-v-w
                    orbit_count[u][2] += 1
                    orbit_count[v][2] += 1
                    orbit_count[w][2] += 1
            
            # Wedges (2-paths) through edge u-v
            # Orbit 0 (ends): for u and v
            wedges_through_uv = (deg_u - 1 - common_neighbors) + (len(adj[v]) - 1 - common_neighbors)
            
            orbit_count[u][0] += (len(adj[v]) - 1 - common_neighbors)   # u as end
            orbit_count[v][0] += (deg_u - 1 - common_neighbors)         # v as end
            
            # Orbit 1 (middle): when going through other neighbors
            orbit_count[u][1] += (deg_u - 1 - common_neighbors)         # u as center for paths through v
            orbit_count[v][1] += (len(adj[v]) - 1 - common_neighbors)

    # Each triangle is counted 6 times (3 nodes × 2 directions), so normalize
    for node in orbit_count:
        orbit_count[node][2] //= 6

    return dict(orbit_count)


def print_orbit_summary(orbit_counts: Dict[int, List[int]]):
    """Print summary of orbit distribution"""
    total_orbit0 = sum(oc[0] for oc in orbit_counts.values())
    total_orbit1 = sum(oc[1] for oc in orbit_counts.values())
    total_orbit2 = sum(oc[2] for oc in orbit_counts.values())

    print(f"\n3-Node Graphlet Orbits Summary:")
    print(f"Orbit 0 (Wedge End)     : {total_orbit0}")
    print(f"Orbit 1 (Wedge Center)  : {total_orbit1}")
    print(f"Orbit 2 (Triangle)      : {total_orbit2}")
    print(f"Total orbit instances   : {total_orbit0 + total_orbit1 + total_orbit2}")


def analyze_graphlets_with_orbits(file_path: str):
    """Full analysis for one graph"""
    print(f"\n=== Graphlet Orbit Analysis: {os.path.basename(file_path)} ===")
    
    adj = read_graph(file_path, undirected=True)
    
    orbit_counts = count_3_node_orbits(adj)
    print_orbit_summary(orbit_counts)
    
    return orbit_counts