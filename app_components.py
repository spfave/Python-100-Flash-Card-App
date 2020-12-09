import tkinter as tk
import app_parameters as ap


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

        self.card = AppCard(parent)

    # todo: create carddeck data
    # todo: save incorrect words

    # todo: get next card in deck
    def next_card(self):
        pass

    # todo: remove word/card from deck if gotten correct


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
