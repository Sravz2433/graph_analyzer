from typing import Dict, Set, List, Tuple
from collections import defaultdict

def find_connected_components(adj: Dict[int, Set[int]]) -> List[Set[int]]:
    """
    Finds all connected components using DFS.
    Returns list of sets, each set is one component.
    """
    visited = set()
    components = []

    def dfs(node: int, component: Set[int]):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.add(current)
                # Add all unvisited neighbors
                for neighbor in adj.get(current, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Find components
    for node in sorted(adj.keys()):
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)

    return components


def print_components(components: List[Set[int]]):
    """Pretty print the components"""
    print(f"\nTotal Connected Components: {len(components)}\n")
    
    for i, comp in enumerate(components, 1):
        nodes = sorted(comp)
        print(f"Group {i} → {{{', '.join(map(str, nodes))}}}")