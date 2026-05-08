import matplotlib.pyplot as plt


def plot_graphlets(
    graphlet_result,
    graph_name,
    ax
):

    labels = ["3-node Paths", "Triangles"]

    values = [
        graphlet_result.get("wedges", 0),
        graphlet_result.get("triangles", 0)
    ]

    ax.bar(
        labels,
        values,
        edgecolor="black"
    )

    ax.set_ylabel("Count")

    ax.set_title(
        f"{graph_name}",
        fontsize=10
    )