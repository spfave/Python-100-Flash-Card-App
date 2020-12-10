import tkinter as tk
# import random
import app_components as ac
import app_parameters as ap
# from language_data import language_fr_dict


# Classes
class MainApplication(tk.Frame):
    """  """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(bg=ap.BACKGROUND_COLOR)
        self.card_deck = ac.CardDeck(self)
        self.timer_flip = None
        # self.lang_from = "French"
        # self.lang_to = "English"

        # self.card = ac.AppCard(self)

        self.image_correct = tk.PhotoImage(file="images/right.png")
        self.button_correct = ac.AppButton(
            self, image=self.image_correct, command=self.click_correct)
        self.image_wrong = tk.PhotoImage(file="images/wrong.png")
        self.button_wrong = ac.AppButton(
            self, image=self.image_wrong, command=self.click_wrong)

        self.card_deck.card.grid(row=0, column=0, columnspan=2)
        self.button_correct.grid(row=1, column=0)
        self.button_wrong.grid(row=1, column=1)

        # self.delay_card_flip()
        # self.refresh_card()

    def click_correct(self):
        # self.refresh_card()
        self.card_deck.next_card()

    def click_wrong(self):
        # self.refresh_card()
        self.card_deck.next_card()

    # todo: refactor to AppCard class
    def refresh_card(self):
        self.after_cancel(self.timer_flip)
        # self.card_data = random.choice(language_fr_dict)

        # self.card.itemconfig(
        #     self.card.image_side, image=self.card.image_front)
        # self.card.itemconfig(
        #     self.card.title, text=self.lang_from, fill="black")
        # self.card.itemconfig(
        #     self.card.word, text=self.card_data[self.lang_from], fill="black")

        # self.delay_card_flip()

    # def delay_card_flip(self):
    #     self.timer_flip = self.after(3000, func=self.flip_card)

    # todo: refactor to AppCard class
    # def flip_card(self):
    #     self.card.itemconfig(self.card.image_side, image=self.card.image_back)
    #     self.card.itemconfig(
    #         self.card.title, text=self.lang_to, fill="white")
    #     self.card.itemconfig(
    #         self.card.word, text=self.card_data[self.lang_to], fill="white")
