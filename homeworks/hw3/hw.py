import pandas as pd

def homework(anime_data, metric_column, n): #Pareto Analysis

    sorted_data = anime_data.sort_values(
        by=metric_column,
        ascending=False
    )

    ranks = sorted_data[metric_column].rank(method="first", ascending=False)

    groups = pd.qcut(ranks, q=n, labels=False)

    proportions = (
        sorted_data
        .groupby(groups)[metric_column]
        .sum()
        / sorted_data[metric_column].sum()
    )

    proportions = proportions.sort_values(ascending=False)

    proportions.index = [
        f"Group {i+1}" for i in range(len(proportions))
    ]

    return proportions