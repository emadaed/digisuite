import tkinter as tk
from playsound import playsound
import threading

# Secret number to guess
secret_number = 777

# Function to play sound without freezing GUI
def play_sound(file):
    threading.Thread(target=lambda: playsound(file)).start()

# Function called when user clicks Submit
def submit():
    global number
    try:
        number = int(entry.get())
        run_game()
    except ValueError:
        result_label.config(text="Please enter a valid integer!", fg="orange")

# Main game loop
def run_game():
    global number
    while number != secret_number:
        result_label.config(text="Ha ha, you are stuck in my loop\n***TRY AGAIN***", fg="red")
        play_sound("wrong.mp3")
        return  # Return so GUI stays responsive
    else:
        result_label.config(text="Well done, you are free now!", fg="green")
        play_sound("congrats.mp3")

# GUI setup
root = tk.Tk()
root.title("Guess the Secret Number")
root.geometry("400x200")

label = tk.Label(root, text="Welcome to my game, muggle!\nEnter an integer number:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=submit, font=("Arial", 12, "bold"))
button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

number = None  # Variable to store user input

root.mainloop()
