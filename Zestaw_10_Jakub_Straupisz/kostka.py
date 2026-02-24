import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    label_result.config(text=str(result))

root = tk.Tk()
root.title("Rzut kostką")
root.configure(bg="black")

label_result = tk.Label(
    root,
    text="?",
    font=("Arial", 40),
    fg="yellow",
    bg="black"
)
label_result.grid(row=0, column=0, padx=100, pady=50)

button = tk.Button(
    root,
    text="Rzuć kostką",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=roll_dice
)
button.grid(row=1, column=0, pady=10)

root.mainloop()
