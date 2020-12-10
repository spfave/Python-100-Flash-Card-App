import pandas as pd


# Functions
def dataframe_to_dict(dataframe):
    return dataframe.to_dict(orient="records")


# Classes
class IOControl():
    """  """

    def __init__(self, lang_from):
        """  """
        self.lang_cards = f"data/{lang_from.lower()}_words2.csv"
        self.lang_cards_reduced = f"data/{lang_from.lower()}_words_to_learn.csv"

    def get_all_cards(self):
        with open(self.lang_cards, mode="r") as data_file:
            cards_data = pd.read_csv(data_file)
            cards_dict = dataframe_to_dict(cards_data)
            return cards_dict

    def get_cards(self):
        try:
            with open(self.lang_cards_reduced, mode="r") as data_file:
                cards_data = pd.read_csv(data_file)
        except FileNotFoundError:
            cards_data = self.get_all_cards()
        finally:
            cards_dict = dataframe_to_dict(cards_data)
            return cards_dict

    def write_cards(self, words_to_learn):
        data_words_to_learn = pd.DataFrame(words_to_learn)
        with open(self.lang_cards_reduced, mode="w", newline="") as write_file:
            data_words_to_learn.to_csv(write_file, index=False)
