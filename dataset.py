import sqlite3
import pandas as pd


def clean_dataset(file_path='./top_rated_movies.csv'):
    df = pd.read_csv(file_path)

    # drop empty rows with missing values
    df.dropna(subset=['release_date', 'vote_average'], inplace=True)

    # format date, popularity, vote_average, vote_count
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['popularity'] = pd.to_numeric(df['popularity'])
    df['vote_average'] = pd.to_numeric(df['vote_average'])
    df['vote_count'] = pd.to_numeric(df['vote_count'])

    # remove duplicates
    df.drop_duplicates()
    
    df.to_csv("movies_cleaned.csv", index=False)
    return df

def insert_to_db(df):
    conn= sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            original_title TEXT,
            overview TEXT,
            release_date DATE,
            popularity FLOAT,
            vote_average FLOAT,
            vote_count INTEGER
        )
        """
    )

    df.to_sql('movies', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


if __name__=='__main__':
    df = clean_dataset()
    insert_to_db(df)