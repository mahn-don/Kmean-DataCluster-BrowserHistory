import pandas as pd
import numpy as np
import nltk
from nltk.stem.snowball import SnowballStemmer
import re
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

import warnings
warnings.filterwarnings('ignore')


'''get data'''
titles1 = open('data/key.txt').read().split('\n')
desc1 = open('data/des.txt',encoding='utf-8').read().split('===')[:-1]
desc1.pop(397)
desc1.pop(397)
titles=[]
desc=[]

for i in range(len(desc1)):
	if desc1[i] !='doanducmanh':
		titles.append(titles1[i])
		desc.append(desc1[i])

# desc = open('newsy.txt',encoding='utf-8').read().split('===')[:-1]

'''Process text'''
stemmer = SnowballStemmer("english")


def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return filtered_tokens
    return stems

def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in desc:
    allwords_stemmed = tokenize_and_stem(i)
    totalvocab_stemmed.extend(allwords_stemmed)
    
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)



'''TF-IDF'''
tfidf_vectorizer = TfidfVectorizer(max_df=0.8,
                                 min_df=0.1, stop_words='english', ngram_range=(1,2))
tfidf_matrix = tfidf_vectorizer.fit_transform(desc)
terms = tfidf_vectorizer.get_feature_names()


'''elbow'''
# sumdn= []
# K= range(1,30)
# for k in K:
# 	km= KMeans(n_clusters=k)
# 	km.fit(tfidf_matrix)
# 	sumdn.append(km.inertia_)

# plt.plot(K, sumdn,'bx-')
# plt.show()



'''Kmean'''
num_clusters = 17
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()


films = { 'title': titles, 'synopsis': desc, 'cluster': clusters }

frame = pd.DataFrame(films, index = [clusters] , columns = ['title', 'cluster'])


# '''Result'''
print("Top terms per cluster:")
order_centroids = km.cluster_centers_.argsort()[:, ::-1]
for i in range(num_clusters):
    
    
    print("Cluster %d:" % i, end='')
    for title in frame.loc[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print()
    print()