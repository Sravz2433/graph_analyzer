import os
import matplotlib.pyplot as plt
from collections import Counter


def generate_combined_degree_distribution(
    degree_data
):
    """
    degree_data format:

    [
        (
            graph_name,
            out_degrees,
            in_degrees
        ),
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

    for idx, (
        graph_name,
        out_degrees,
        in_degrees
    ) in enumerate(degree_data):

        ax = axes[idx]

        # ================= Degree Counts =================
        out_counter = Counter(out_degrees)

        in_counter = Counter(in_degrees)

        # ================= Sorted Keys =================
        out_x = sorted(out_counter.keys())
        out_y = [out_counter[d] for d in out_x]

        in_x = sorted(in_counter.keys())
        in_y = [in_counter[d] for d in in_x]

        # ================= Plot =================
        ax.bar(
            out_x,
            out_y,
            alpha=0.7,
            label="Out-Degree"
        )

        ax.plot(
            in_x,
            in_y,
            marker='o',
            linewidth=2,
            label="In-Degree"
        )

        ax.set_title(
            graph_name,
            fontsize=10
        )

        ax.set_xlabel("Degree")

        ax.set_ylabel("Node Count")

        ax.legend(fontsize=8)

    # ================= Remove Empty Axes =================
    if len(degree_data) < len(axes):

        for j in range(len(degree_data), len(axes)):
            fig.delaxes(axes[j])

    plt.tight_layout()

    save_path = (
        "results/combined_degree_distribution.png"
    )

    plt.savefig(
        save_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(
        f"Combined degree distribution saved: {save_path}"
    )

    return save_path