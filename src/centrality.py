import networkx as nx

def compute_centrality(adj):

    G = nx.DiGraph()

    for u in adj:
        for v in adj[u]:
            G.add_edge(u, v)

    degree_cent = nx.degree_centrality(G)
    betweenness_cent = nx.betweenness_centrality(G)

    return degree_cent, betweenness_cent


def top_k(dictionary, k=5):
    return sorted(
        dictionary.items(),
        key=lambda x: x[1],
        reverse=True
    )[:k]