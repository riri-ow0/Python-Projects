import random
import tkinter as tk

root = tk.Tk()
root.title("20-sided Die")
root.geometry("320x220")
root.resizable(True, True)

header_label = tk.Label(root, text="20-sided Die", font=("Comic Sans MS", 18, "bold"))
header_label.pack(pady=(15, 5))

result_label = tk.Label(root, text="Press Roll to begin!", font=("Comic Sans MS", 12))
result_label.pack(pady=5)

status_label = tk.Label(root, text="", font=("Comic Sans MS", 11))
status_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)


def roll_die():
    roll = random.randint(1, 20)

    if roll < 15:
        result_label.config(text=f"You rolled: {roll}!", fg="black")
        status_label.config(text="Your attack is INEFFECTIVE.", fg="red")
    elif roll >= 15 and roll <= 19 :
        result_label.config(text=f"You rolled: {roll}!", fg="black")
        status_label.config(text="Your attack is EFFECTIVE!", fg="green")
    elif roll == 20:
        result_label.config(text=f"You rolled: {roll}!", fg="black")
        status_label.config(text="Your attack is SUPER EFFECTIVE!", fg="blue")


def quit_app():
    root.destroy()


roll_button = tk.Button(button_frame, text="Roll", font=("Comic Sans MS", 12), width=10, command=roll_die)
roll_button.grid(row=0, column=0, padx=5)

quit_button = tk.Button(button_frame, text="Exit", font=("Comic Sans MS", 12), width=10, command=quit_app)
quit_button.grid(row=0, column=1, padx=5)

root.mainloop()
