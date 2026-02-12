import duckdb
import pandas as pd

DB_PATH = "warehouse/civic311.duckdb"


def load_to_duckdb(df: pd.DataFrame):
    con = duckdb.connect(DB_PATH)

    con.execute("""
        CREATE TABLE IF NOT EXISTS requests AS
        SELECT * FROM df LIMIT 0
    """)

    con.execute("INSERT INTO requests SELECT * FROM df")

    con.close()
