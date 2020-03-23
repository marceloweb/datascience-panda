import pandas as pd

rating = pd.read_csv('data/ratings.csv')
rating.head()
rating.shape
rating['rating'].value_counts()
print(rating['rating'].mean())
print(rating['rating'].median())

rating.rating.plot(kind='hist')
print(rating.rating.describe())
