# Mini ETL for Postgres using Pandas

# Dependencies
import pandas as pd
import json
from sqlalchemy import create_engine
import os
from transform_steps.cleaning import cleaning_merge

# Environmental variables for password and user for local testing
db_demo_secret = os.environ.get('DB_DEMO_SECRET')
db_demo_user = os.environ.get('DB_DEMO_USER')

# Data sources
csv_games = ("./Resources/SteamCharts.csv")
with open("./Resources/steam-reviews.json", 'r', encoding="utf-8") as reviews:
    json_games = json.load(reviews)

#### Extraction (format conversion)
def extract_data_csv(csv_data):
    df_csv_raw = pd.read_csv(csv_data, encoding="unicode_escape")
    return df_csv_raw

def extract_data_json(json_data):
    df_json_raw = pd.json_normalize(json_data)
    return df_json_raw

#### Transformation (cleaning.py)
def transform_data(df_csv_raw, df_json_raw):
    merge_df = cleaning_merge(df_csv_raw, df_json_raw)
    return merge_df

#### Load
def load_data(merge_df, db_demo_user, db_demo_secret):
    # Connect to postgres
    engine = create_engine(f'postgresql://{db_demo_user}:{db_demo_secret}@localhost:5433/steam')
    connection = engine.connect()
    # Load merged dataframe (replace data in table)
    merge_df.to_sql(name="game_data", con=engine, if_exists="replace", index=False)
    print(f"Complete! Total rows = {len(merge_df.index)}")
    return None

#### Main ETL Function
def etl_steps(csv_data, json_data, db_demo_user, db_demo_secret):
    # Extraction (format conversion)
    print("Converting csv data...")
    df_csv_raw = extract_data_csv(csv_data)
    print("Converting json data...")
    df_json_raw = extract_data_json(json_data)

    # Transformation (cleaning)
    print("Transforming and merging data...")
    merge_df = cleaning_merge(df_csv_raw, df_json_raw)
    
    # Loading
    print("Loading data...")
    load_data(merge_df, db_demo_user, db_demo_secret)
    return None

# Run main function
etl_steps(csv_games, json_games, db_demo_user, db_demo_secret)