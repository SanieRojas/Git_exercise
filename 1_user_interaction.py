
import pandas as pd 
from word_checker.data_import import load_word2vec_model, get_word_list

model = load_word2vec_model()
words_list = get_word_list(model)

user_input = input("Please, ask for word similarities. What word would you like to explore? ")

if user_input in words_list:
    print("Most similar words identified:", pd.DataFrame(model.most_similar(user_input, topn=10))),
else: print("Word not covered in this model")
