import pandas as pd


# Language data import
language_fr_data = pd.read_csv("data/french_words.csv")
language_fr_dict = language_fr_data.to_dict(orient="records")


# todo: Create IOControl class with methods to ...
class IOControl():
    """  """

    def __init__(self, lang_from):
        """  """
        self.lang_cards = f"data/{lang_from}_words.csv"
        self.lang_cards_reduced = f"data/{lang_from}_words_to_learn.csv"

# todo: try to open 'french_words_to_learn.csv' if doesn't exist open 'french-words.csv'
    def get_cards(self):
        try:
            with open(self.lang_cards_reduced, mode="r") as data_file:
                cards_data = pd.read_csv(data_file)
        except FileNotFoundError:
            with open(self.lang_cards, mode="r") as data_file:
                cards_data = pd.read_csv(data_file)
        finally:
            cards_dict = cards_data.to_dict(orient="records")
            return cards_dict

# todo: save incorrect words to 'french_words_to_learn.csv'
    def write_cards(self, words_to_learn):
        with open(self.lang_cards_reduced, mode="w") as write_file:
            words_to_learn.to_csv(write_file, index=False)
