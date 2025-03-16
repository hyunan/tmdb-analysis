import sqlite3
import pandas as pd


def load_dataset(file_path='./top_rated_movies.csv'):
    df = pd.read_csv(file_path)

    conn = sqlite3.connect('movie_database.db')
    df.to_sql('movies', conn, if_exists='replace', index=False)

    conn.close()
    print("CSV data imported successfully.")
    return df

df = load_dataset()
print(df.head())