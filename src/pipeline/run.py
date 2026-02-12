from extract import fetch_311_data
from transform import clean_311_data
from load import load_to_duckdb


def run_pipeline():
    raw_df = fetch_311_data(7)
    clean_df = clean_311_data(raw_df)
    load_to_duckdb(clean_df)


if __name__ == "__main__":
    run_pipeline()
