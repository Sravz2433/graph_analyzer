from collections import defaultdict
from typing import Dict, Set

def read_graph(file_path: str, undirected: bool = True) -> Dict[int, Set[int]]:
    """
    Reads graph from file and returns adjacency list (using sets to avoid duplicate edges)
    """
    adj = defaultdict(set)
    
    with open(file_path, 'r') as f:
        N = int(f.readline().strip())
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                u, v = int(parts[0]), int(parts[1])
                adj[u].add(v)
                if undirected:
                    adj[v].add(u)
    
    # Add isolated nodes
    for i in range(N):
        if i not in adj:
            adj[i] = set()
    
    return dict(adj)