
print("Succesful process initiation...")

#importing and loading word2vec model with word embeddings
import gensim.downloader as api
import pandas as pd 

model = api.load('word2vec-google-news-300')
print("Model Word2Vec succesfully loaded")


words_list = list(model.index_to_key)
print("Words listed sucessfully for analysis")



user_input = input("Please, ask for word similarities. What word would you like to explore? ")

if user_input in words_list:
    print("Most similar words identified:", pd.DataFrame(model.most_similar(user_input, topn=10))),
else: print("Word not covered in this model")


