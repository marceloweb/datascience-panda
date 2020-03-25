import pandas as pd
import seaborn as sns

rating = pd.read_csv('data/ratings.csv')
rating.head()
rating.shape
rating['rating'].value_counts()
print(rating['rating'].mean())
print(rating['rating'].median())
print(rating.query("movieId==1").rating.median())

rating.rating.plot(kind='hist')
print(rating.rating.describe())

sns.boxplot(rating.rating)

movies = pd.read_csv('data/movies.csv')
movies.head()
