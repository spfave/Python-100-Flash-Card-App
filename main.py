import tkinter as tk
import application_main as am
import app_parameters as ap


# Main
root = tk.Tk()
root.title("Language Flash Cards")
root.minsize(width=900, height=700)
root.config(padx=50, pady=50, bg=ap.BACKGROUND_COLOR)

flash_card_app = am.MainApplication(root)
flash_card_app.place(anchor="center", relx=.5, rely=.5)

root.mainloop()
