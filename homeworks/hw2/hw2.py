import pandas as pd


def homework(anime_data_extracted: pd.DataFrame) -> pd.Series:
    
    return (anime_data_extracted
            .groupby("Type")
            ["Score"].mean()
            .sort_values(ascending=False)
            )
