import matplotlib.pyplot as plt
import os

from src.graph_visualizer import visualize_graph


def generate_combined_figure(graph_data):

    """
    graph_data:
    [
        (adj, graph_name),
        ...
    ]
    """

    os.makedirs("results", exist_ok=True)

    fig, axes = plt.subplots(
        2,
        3,
        figsize=(18, 10)
    )

    axes = axes.flatten()

    for idx, (adj, graph_name) in enumerate(graph_data):

        visualize_graph(
            adj=adj,
            ax=axes[idx],
            graph_name=graph_name
        )

    # Remove unused subplot
    if len(graph_data) < len(axes):
        for j in range(len(graph_data), len(axes)):
            fig.delaxes(axes[j])

    plt.tight_layout()

    save_path = "results/combined_graph_visualizations.png"

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Combined visualization saved: {save_path}")

    return save_path