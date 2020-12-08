import tkinter as tk
import app_components as ac
import app_parameters as ap


# Classes
class MainApplication(tk.Frame):
    """  """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(bg=ap.BACKGROUND_COLOR)

        self.canvas_card = ac.AppCardCanvas(self, width=800, height=526,
                                            bg=ap.BACKGROUND_COLOR,
                                            highlightthickness=0)
        self.image_card = tk.PhotoImage(file="images/card_front.png")
        self.canvas_card.create_image(400, 263, image=self.image_card)

        self.button_correct = ac.AppButton(self, text="Correct")
        self.button_wrong = ac.AppButton(self, text="Wrong")

        self.canvas_card.grid(row=0, column=0, columnspan=2)
        self.button_correct.grid(row=1, column=0)
        self.button_wrong.grid(row=1, column=1)
