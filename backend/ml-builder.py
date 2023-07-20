import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt
import seaborn as sns
import nltk 
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv('./data/movies.csv')
df.drop_duplicates(subset=['title', 'release_date'], inplace=True)

df1 = df[df.vote_count >= 20].reset_index()

df1.fillna('', inplace=True)

index = df1[(df1['genres'] == '') & (df1['overview'] == '')].index
df1.drop(index, inplace=True)

df1['genres'] = df1['genres'].apply(lambda x: ' '.join(x.split('-')))
df1['keywords'] = df1['keywords'].apply(lambda x: ' '.join(x.split('-')))
df1['credits'] = df1['credits'].apply(lambda x: ' '.join(x.replace(' ', '').split('-')[:5]))

df1['tags'] = df1['overview'] + ' ' + df1['genres'] + ' ' + df1['keywords'] + ' ' + df1['credits'] + ' ' + df1['original_language']

def stem(text):
    y = []
    for i in text.split():
        y.append(SnowballStemmer('english').stem(i))
    return ' '.join(y)

stemmer = SnowballStemmer('english')

df1['tags'] = df1['tags'].apply(stem)
df1['tags'] = df1['tags'].str.replace('[^\w\s]', '')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df1['tags'])

print("pickle dump")
pickle.dump(tfidf_matrix, open('./data/tfidf_matrix.pkl', 'wb'))
pickle.dump(df1, open('./data/movie_list.pkl', 'wb'))
print("pickle dump done")
