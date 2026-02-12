import pandas as pd


def clean_311_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    df["closed_date"] = pd.to_datetime(df["closed_date"], errors="coerce")

    df["close_duration_hours"] = (
        df["closed_date"] - df["created_date"]
    ).dt.total_seconds() / 3600

    df["agency"] = df["agency"].str.upper().str.strip()
    df["borough"] = df["borough"].str.upper().str.strip()

    return df
