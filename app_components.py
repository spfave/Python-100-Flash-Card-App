import tkinter as tk
import random
import app_parameters as ap
import io_control as io


# Constants
FONT_NAME = "Arial"


# Variables
font_lang = (FONT_NAME, 50, "italic")
font_word = (FONT_NAME, 60, "bold")


# Classes
class CardDeck():
    """  """

    def __init__(self, parent):
        self.lang_from = "French"
        self.lang_to = "English"
        self.io = io.IOControl(self.lang_from)
        self.cards = self.io.get_cards()
        self.card = AppCard(parent)
        self.next_card()

    def next_card(self):
        self.card.refresh(random.choice(self.cards), self.lang_from)

    def remove_card(self):
        self.cards[:] = [
            card for card in self.cards
            if card.get(self.lang_to) != self.card.get_word_text(self.lang_to)]

        if len(self.cards) == 0:  # start with full deck again
            card_data = self.io.get_all_cards()
            self.cards = io.dataframe_to_dict(card_data)

    def save_words_to_learn(self):
        self.io.write_cards(self.cards)


class AppCard(tk.Canvas):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(width=800, height=526,
                    bg=ap.BACKGROUND_COLOR,
                    highlightthickness=0)

        self.image_front = tk.PhotoImage(file="images/card_front.png")
        self.image_back = tk.PhotoImage(file="images/card_back.png")
        self.image_side = self.create_image(400, 263, image=None)
        self.title = self.create_text(400, 155, text="", font=font_lang)
        self.word = self.create_text(400, 325, text="", font=font_word)

    def refresh(self, card_data, lang_from):
        self.data = card_data

        self.itemconfig(self.image_side, image=self.image_front)
        self.itemconfig(self.title, text=lang_from, fill="black")
        self.itemconfig(
            self.word, text=self.data[lang_from], fill="black")

    def flip(self, lang_to):
        self.itemconfig(self.image_side, image=self.image_back)
        self.itemconfig(self.title, text=lang_to, fill="white")
        self.itemconfig(self.word, text=self.data[lang_to], fill="white")

    def get_word_text(self, lang):
        return self.data.get(lang)


class AppButton(tk.Button):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(
            background=ap.BACKGROUND_COLOR,
            activebackground=ap.BACKGROUND_COLOR,
            relief="flat",
            highlightthickness=0
        )
