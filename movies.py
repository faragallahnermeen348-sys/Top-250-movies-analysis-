import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\User\Downloads\tsMovies.csv")



#histgraph of distribution of movie ratings :)

plt.hist(df["Rating"], bins=15, color="#E6E6FA", edgecolor="black")
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

#bar chart of top 10 directors by average rating :)

director_avg = df.groupby("Director")["Rating"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,10))
plt.xlim(8.5, 9)
plt.barh(director_avg.index, director_avg.values, color="skyblue")
plt.title("Top 10 Directors by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Director")
plt.gca().invert_yaxis()
plt.show()

#line graph of how many movies released each year :)

movies_per_year = df["Released_year"].value_counts().sort_index()
plt.figure(figsize=(18,6))


above_5 = movies_per_year[movies_per_year.values > 5]
below_5 = movies_per_year[movies_per_year.values <= 5]


plt.plot(movies_per_year.index, movies_per_year.values,
         color="lightgray")

plt.scatter(below_5.index, below_5.values,
            color="red",
            label="≤ 5 movies")


plt.scatter(above_5.index, above_5.values,
            color="green",
            label="> 5 movies")

plt.axhline(5, color="black", linestyle="--", linewidth=1)
plt.title("Movies Released Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.show()




