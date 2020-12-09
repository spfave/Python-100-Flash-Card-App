import pandas as pd


# Language data import
language_fr_data = pd.read_csv("data/french_words.csv")
language_fr_dict = language_fr_data.to_dict(orient="records")
# print(language_fr_dict)


# todo: Create IOControl class with methods to ...
# todo: try to open 'french_words_to_learn.csv' if doesn't exist open 'french-words.csv'


# todo: save incorrect words to 'french_words_to_learn.csv'
