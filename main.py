import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")
netflix_subset = netflix_df[netflix_df["type"] != "TV Show"]
netflix_subset.head()
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]
netflix_movies.head()
short_movies = netflix_movies[netflix_movies["duration"] < 60]
short_movies.head()

colors = []
for label, row in netflix_movies.iterrows() :
    genre = row["genre"]
    
    if genre == "Children":
        color = "blue"
    elif genre == "Documentaries":
        color = "green"
    elif genre == "Stand-Up":
        color = "red"
    else:
        color = "black"
    colors.append(color)

colors[:10]
    
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()

answer = "no"
