import pandas as pd


# Language data import
language_fr_data = pd.read_csv("data/french_words.csv")
language_fr_dict = language_fr_data.to_dict(orient="records")
# print(language_fr_dict)
