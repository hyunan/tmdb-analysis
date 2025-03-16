import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
conn = sqlite3.connect("movies.db")

# Function to run SQL queries and return DataFrame
def run_query(query):
    return pd.read_sql_query(query, conn)


query = """
SELECT strftime('%Y', release_date) AS year, AVG(vote_average) AS avg_rating
FROM movies
GROUP BY year
ORDER BY year ASC;
"""
df = run_query(query)

# Plot the results
plt.figure(figsize=(12, 5))
sns.lineplot(data=df, x="year", y="avg_rating", marker="o", color="red")
plt.title("Average Movie Ratings Over Time")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.xticks(rotation=90)
plt.grid()
plt.show()