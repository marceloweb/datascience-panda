import pandas as pd

rating = pd.read_csv('data/ratings.csv')
rating.head()
rating.shape
rating['rating'].value_counts()
rating['rating'].mean()

rating.rating.plot(kind='hist')
