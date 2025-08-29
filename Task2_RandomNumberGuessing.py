import tkinter as tk
import random
from tkinter import messagebox

# Generate random number
number = random.randint(1, 50)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < number:
            result.set("Too low! Try again.")
        elif guess > number:
            result.set("Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {number} in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number.")

def reset_game():
    global number, attempts
    number = random.randint(1, 50)
    attempts = 0
    entry.delete(0, tk.END)
    result.set("New game started! Guess a number between 1 and 50.")

# Tkinter Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")
root.configure(bg="#1e1e2f")

title = tk.Label(root, text="Number Guessing Game", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2f")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

btn = tk.Button(root, text="Check Guess", command=check_guess, bg="#4CAF50", fg="white", font=("Arial", 12))
btn.pack(pady=10)

result = tk.StringVar()
result.set("Guess a number between 1 and 50.")
label_result = tk.Label(root, textvariable=result, font=("Arial", 12), fg="cyan", bg="#1e1e2f")
label_result.pack(pady=10)

root.mainloop()
