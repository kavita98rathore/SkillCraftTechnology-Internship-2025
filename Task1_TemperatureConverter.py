import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def convert_temperature():
    try:
        temp = float(entry_temp.get())
        scale = combo_scale.get()

        if scale == "Celsius":
            f = celsius_to_fahrenheit(temp)
            k = celsius_to_kelvin(temp)
            result.set(f"Fahrenheit: {f:.2f} °F | Kelvin: {k:.2f} K")

        elif scale == "Fahrenheit":
            c = fahrenheit_to_celsius(temp)
            k = fahrenheit_to_kelvin(temp)
            result.set(f"Celsius: {c:.2f} °C | Kelvin: {k:.2f} K")

        elif scale == "Kelvin":
            c = kelvin_to_celsius(temp)
            f = kelvin_to_fahrenheit(temp)
            result.set(f"Celsius: {c:.2f} °C | Fahrenheit: {f:.2f} °F")

        else:
            messagebox.showerror("Error", "Please select a valid scale.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.configure(bg="#1e1e2f")


title = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2f")
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Label(frame, text="Enter Temperature:", fg="white", bg="#1e1e2f").grid(row=0, column=0, padx=5, pady=5)
entry_temp = tk.Entry(frame, width=10)
entry_temp.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Select Scale:", fg="white", bg="#1e1e2f").grid(row=1, column=0, padx=5, pady=5)
combo_scale = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_scale.grid(row=1, column=1, padx=5, pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert_temperature, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_convert.pack(pady=10)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="cyan", bg="#1e1e2f")
result_label.pack(pady=10)

root.mainloop()
