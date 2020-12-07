import tkinter as tk
import app_components as ac


# Main
root = tk.Tk()
root.title("Language Flash Cards")
root.minsize(width=300, height=300)

button_correct = ac.AppButton(text="Correct")
button_correct.pack()


root.mainloop()
