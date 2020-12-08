import tkinter as tk
import random
import app_components as ac
import app_parameters as ap
from language_data import language_fr_dict


# Constants
FONT_NAME = "Arial"


# Variables
font_lang = (FONT_NAME, 50, "italic")
font_word = (FONT_NAME, 60, "bold")


# Classes
class MainApplication(tk.Frame):
    """  """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(bg=ap.BACKGROUND_COLOR)
        self.language = "French"

        self.canvas_card = ac.AppCardCanvas(self, width=800, height=526,
                                            bg=ap.BACKGROUND_COLOR,
                                            highlightthickness=0)
        self.image_card_front = tk.PhotoImage(file="images/card_front.png")
        self.image_card_back = tk.PhotoImage(file="images/card_back.png")
        self.card_side = self.canvas_card.create_image(
            400, 263, image=self.image_card_front)
        self.card_title = self.canvas_card.create_text(
            400, 155, text="", font=font_lang)
        self.card_word = self.canvas_card.create_text(
            400, 325, text="", font=font_word)
        self.new_word()

        self.image_correct = tk.PhotoImage(file="images/right.png")
        self.button_correct = ac.AppButton(
            self, image=self.image_correct, command=self.click_correct)
        self.image_wrong = tk.PhotoImage(file="images/wrong.png")
        self.button_wrong = ac.AppButton(
            self, image=self.image_wrong, command=self.click_wrong)

        self.canvas_card.grid(row=0, column=0, columnspan=2)
        self.button_correct.grid(row=1, column=0)
        self.button_wrong.grid(row=1, column=1)

    def click_correct(self):
        self.new_word()
        self.flip_card()

    def click_wrong(self):
        self.new_word()

    def new_word(self):
        """  """
        card_data = random.choice(language_fr_dict)
        self.canvas_card.itemconfig(self.card_title, text=self.language)
        self.canvas_card.itemconfig(
            self.card_word, text=card_data[self.language])

    def flip_card(self):
        self.canvas_card.itemconfig(self.card_side, image=self.image_card_back)
