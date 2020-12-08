import tkinter as tk
import application_main as am
import app_components as ac
import app_parameters as ap


# Main
root = tk.Tk()
root.title("Language Flash Cards")
root.minsize(width=300, height=300)
root.config(padx=20, pady=20, bg=ap.BACKGROUND_COLOR)

flash_card_app = am.MainApplication(root)
flash_card_app.pack()
# button_correct = ac.AppButton(text="Correct")
# button_correct.pack()

# canvas_card = tk.Canvas(root, width=800, height=526)
# image_card = tk.PhotoImage(file="images/card_front.png")
# canvas_card.create_image(400, 263, image=image_card)
# canvas_card.pack()

# canvas_card = ac.AppCardCanvas(root, width=800, height=526)
# image_card = tk.PhotoImage(file="images/card_front.png")
# canvas_card.create_image(400, 263, image=image_card)
# canvas_card.pack()


root.mainloop()
