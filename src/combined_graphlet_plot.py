import os
import matplotlib.pyplot as plt

from src.graphlet_plot import plot_graphlets


def generate_combined_graphlet_figure(
    graphlet_data
):

    """
    graphlet_data:
    [
        (graph_name, graphlet_result),
        ...
    ]
    """

    os.makedirs("results", exist_ok=True)

    fig, axes = plt.subplots(
        2,
        3,
        figsize=(15, 10)
    )

    axes = axes.flatten()

    for idx, (graph_name, result) in enumerate(graphlet_data):

        plot_graphlets(
            graphlet_result=result,
            graph_name=graph_name,
            ax=axes[idx]
        )

    # Remove unused subplot
    if len(graphlet_data) < len(axes):

        for j in range(len(graphlet_data), len(axes)):
            fig.delaxes(axes[j])

    plt.tight_layout()

    save_path = (
        "results/combined_graphlet_analysis.png"
    )

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        f"Combined graphlet figure saved: {save_path}"
    )

    return save_path