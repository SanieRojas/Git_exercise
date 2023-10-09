
import pandas as pd 
from Word_Checker import model
from Word_Checker import words_list

user_input = input("Please, ask for word similarities. What word would you like to explore? ")

if user_input in words_list:
    print("Most similar words identified:", pd.DataFrame(model.most_similar(user_input, topn=10))),
else: print("Word not covered in this model")
