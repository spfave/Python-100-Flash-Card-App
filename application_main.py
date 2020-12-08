import tkinter as tk
import app_components as ac
import app_parameters as ap


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

        self.canvas_card = ac.AppCardCanvas(self, width=800, height=526,
                                            bg=ap.BACKGROUND_COLOR,
                                            highlightthickness=0)
        self.image_card_front = tk.PhotoImage(file="images/card_front.png")
        self.canvas_card.create_image(400, 263, image=self.image_card_front)
        self.canvas_card.create_text(400, 155, text="French", font=font_lang)
        self.canvas_card.create_text(400, 325, text="Word", font=font_word)

        self.image_correct = tk.PhotoImage(file="images/right.png")
        self.button_correct = ac.AppButton(self, image=self.image_correct)
        self.image_wrong = tk.PhotoImage(file="images/wrong.png")
        self.button_wrong = ac.AppButton(self, image=self.image_wrong)

        self.canvas_card.grid(row=0, column=0, columnspan=2)
        self.button_correct.grid(row=1, column=0)
        self.button_wrong.grid(row=1, column=1)
