from typing import Dict, Set, List
from collections import defaultdict

class SCCFinder:
    """
    Finds Strongly Connected Components using Kosaraju's Algorithm
    with ITERATIVE DFS to handle large graphs (no recursion limit issues)
    """
    
    def __init__(self, adj: Dict[int, Set[int]]):
        self.adj = adj
        self.adj_rev = self._build_reverse_graph()
        self.visited = set()
        self.stack = []
        self.scc = []

    def _build_reverse_graph(self) -> Dict[int, Set[int]]:
        rev = defaultdict(set)
        for u in self.adj:
            for v in self.adj[u]:
                rev[v].add(u)
        for u in self.adj:
            if u not in rev:
                rev[u] = set()
        return dict(rev)

    def _dfs_iterative(self, graph: Dict[int, Set[int]], start_node: int, use_stack: bool = False):
        """Iterative DFS"""
        stack = [start_node]
        component = set()
        
        while stack:
            node = stack[-1]
            
            if node not in self.visited:
                self.visited.add(node)
                component.add(node)
                
                # Push neighbors
                for neighbor in graph.get(node, []):
                    if neighbor not in self.visited:
                        stack.append(neighbor)
            else:
                # Backtrack
                if use_stack:
                    self.stack.append(node)
                stack.pop()
        
        return component

    def find_scc(self) -> List[Set[int]]:
        self.visited.clear()
        self.stack.clear()
        self.scc.clear()

        # Step 1: Fill stack with finishing times (Iterative DFS on original graph)
        for node in sorted(self.adj.keys()):
            if node not in self.visited:
                self._dfs_iterative(self.adj, node, use_stack=True)

        # Step 2: Process in reverse finishing order on transpose graph
        self.visited.clear()

        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                component = self._dfs_iterative(self.adj_rev, node)
                self.scc.append(component)

        return self.scc


def print_scc(scc_list: List[Set[int]]):
    print(f"\nTotal Strongly Connected Components: {len(scc_list)}\n")
    for i, component in enumerate(scc_list, 1):
        nodes = sorted(component)
        print(f"SCC {i} → Size = {len(component):4d} | Nodes = {nodes[:10]}{'...' if len(nodes)>10 else ''}")


def find_strongly_connected_components(adj: Dict[int, Set[int]]) -> List[Set[int]]:
    scc_finder = SCCFinder(adj)
    return scc_finder.find_scc()