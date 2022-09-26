# # Mini ETL for Postgres using Pandas - Cleaning Steps

# Dependencies
import pandas as pd
import json

# Main function
def cleaning_merge(csv_df, json_df):

#### CSV prep
    # Ignore chained assignment warnings (we want to modify the original dataframe and are not preserving raw)
    pd.options.mode.chained_assignment = None 
    # Rename columns
    csv_df = csv_df.rename(columns={"gamename": "game", 
                                    "year": "year", 
                                    "month": "month", 
                                    "avg": "avg_players",
                                    "gain": "monthly_change",
                                    "peak": "max_players", 
                                    "avg_peak_perc": "avg_max_percent"})

    # Convert NaN to zero for monthly_change column
    csv_df["monthly_change"] = csv_df["monthly_change"].fillna(0)

#### JSON prep
    # Drop columns with missing data
    json_df = json_df[["name", "developer", "price", "full_desc.desc"]]

    # Clean price column (fill NaN to zero, replace "free" with zero, convert to numeric)
    json_df["price"] = json_df["price"].fillna(0)
    json_df["price"] = json_df["price"].replace("free", 0)
    json_df["price"] = pd.to_numeric(json_df["price"])

    # Clean developer column to drop rows with non-ASCII characters
    json_df["developer"] = json_df["developer"].fillna("None")
    json_df = json_df[json_df['developer'].str.contains('[A-Za-z]')]

    # Clean name column to drop rows with non-standard characters or replace with empty
    json_df["name"] = json_df["name"].fillna("None")
    json_df = json_df[json_df['name'].str.contains('[A-Za-z]')]
    json_df["name"] = json_df["name"].str.replace("™", "").str.replace("®", "").str.replace("仁王", "")

    # Convert text data to string
    json_df["name"] = json_df["name"].astype(str)
    json_df["developer"] = json_df["developer"].astype(str)
    json_df["full_desc.desc"] = json_df["full_desc.desc"].astype(str)

    # Remove "About this game" text before string in description column
    json_df["full_desc.desc"] = json_df["full_desc.desc"].str[16:]

    # Rename columns
    json_df = json_df.rename(columns={"name": "game", "developer": "developer", 
                                    "price": "price_cents", "full_desc.desc": "description"})

#### Merging Dataframes
    # Inner join to determine game names in common
    merge_df = pd.merge(csv_df, json_df, on="game", how="inner")

    # Copy index to a column and name as id (will be used as primary key in SQL)
    merge_df.sort_index()
    merge_df.reset_index(inplace=True)
    merge_df = merge_df.rename(columns = {'index':'id'})

    # Return transformed data
    return merge_df