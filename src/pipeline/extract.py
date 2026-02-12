import requests
import pandas as pd
from datetime import datetime, timedelta

API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"

def fetch_311_data(days_back: int = 7) -> pd.DataFrame:
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days_back)

    params = {
        "$where": f"created_date >= '{start_date.isoformat()}'",
        "$limit": 50000
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    df = pd.read_csv(pd.compat.StringIO(response.text))
    return df


if __name__ == "__main__":
    df = fetch_311_data(3)
    print(df.head())
