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

    # image_card_front = tk.PhotoImage(file="images/card_front.png")
    # image_card_back = tk.PhotoImage(file="images/card_back.png")

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(bg=ap.BACKGROUND_COLOR)
        self.timer_flip = None
        self.lang_from = "French"
        self.lang_to = "English"

        self.canvas_card = ac.AppCardCanvas(self, width=800, height=526,
                                            bg=ap.BACKGROUND_COLOR,
                                            highlightthickness=0)
        self.image_card_front = tk.PhotoImage(file="images/card_front.png")
        self.image_card_back = tk.PhotoImage(file="images/card_back.png")
        self.card_side = self.canvas_card.create_image(
            400, 263, image=None)
        self.card_title = self.canvas_card.create_text(
            400, 155, text="", font=font_lang)
        self.card_word = self.canvas_card.create_text(
            400, 325, text="", font=font_word)

        self.image_correct = tk.PhotoImage(file="images/right.png")
        self.button_correct = ac.AppButton(
            self, image=self.image_correct, command=self.click_correct)
        self.image_wrong = tk.PhotoImage(file="images/wrong.png")
        self.button_wrong = ac.AppButton(
            self, image=self.image_wrong, command=self.click_wrong)

        self.canvas_card.grid(row=0, column=0, columnspan=2)
        self.button_correct.grid(row=1, column=0)
        self.button_wrong.grid(row=1, column=1)

        self.delay_card_flip()
        self.new_card()

    def click_correct(self):
        self.new_card()

    def click_wrong(self):
        self.new_card()

    def new_card(self):
        self.after_cancel(self.timer_flip)
        self.card_data = random.choice(language_fr_dict)

        self.canvas_card.itemconfig(
            self.card_side, image=self.image_card_front)
        self.canvas_card.itemconfig(
            self.card_title, text=self.lang_from, fill="black")
        self.canvas_card.itemconfig(
            self.card_word, text=self.card_data[self.lang_from], fill="black")

        self.delay_card_flip()

    def delay_card_flip(self):
        self.timer_flip = self.after(3000, func=self.flip_card)

    def flip_card(self):
        self.canvas_card.itemconfig(self.card_side, image=self.image_card_back)
        self.canvas_card.itemconfig(
            self.card_title, text=self.lang_to, fill="white")
        self.canvas_card.itemconfig(
            self.card_word, text=self.card_data[self.lang_to], fill="white")
