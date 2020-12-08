import tkinter as tk
import application_main as am
import app_components as ac
import app_parameters as ap


# Main
root = tk.Tk()
root.title("Language Flash Cards")
root.minsize(width=850, height=675)
root.config(padx=20, pady=20, bg=ap.BACKGROUND_COLOR)

flash_card_app = am.MainApplication(root)
flash_card_app.place(anchor="center", relx=.5, rely=.5)


root.mainloop()
