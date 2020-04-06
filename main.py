import pandas as pd
import seaborn as sns

rating = pd.read_csv('data/ratings.csv')
rating.head()
rating.shape
rating['rating'].value_counts()
print(rating['rating'].mean())
print(rating['rating'].median())
print(rating.query("movieId==1").mean()['rating'])

rating.rating.plot(kind='hist')
print(rating.rating.describe())

sns.boxplot(rating.rating)

movies = pd.read_csv('data/movies.csv')
movies.head()

tmdb = pd.read_csv('data/tmdb_5000_movies.csv')
tmdb.head()
tmdb.original_language.unique()
# Serie

count_language = tmdb["original_language"].value_counts().to_frame().reset_index()
count_language.columns = ["original_language","total"]
count_language.head()
