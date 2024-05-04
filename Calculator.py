import tkinter as tk
from tkinter import messagebox
import math

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entry():
    entry.delete(0, tk.END)

def add_to_entry(text):
    entry.insert(tk.END, text)

def calculate_sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Scientific Calculator")

# Customizing the background color
root.config(bg="#f0f0f0")

# Entry widget
entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 18), bg="#fff", fg="#333")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=15)

# Buttons layout and styling
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("√", 5, 1)
]

for button_text, r, c in buttons:
    if button_text == "=":
        tk.Button(root, text=button_text, padx=38, pady=20, font=("Arial", 14), bg="#007bff", fg="#fff", command=evaluate_expression).grid(row=r, column=c, pady=5)
    elif button_text == "C":
        tk.Button(root, text=button_text, padx=36, pady=20, font=("Arial", 14), bg="#dc3545", fg="#fff", command=clear_entry).grid(row=r, column=c, pady=5)
    elif button_text == "√":
        tk.Button(root, text=button_text, padx=36, pady=20, font=("Arial", 14), bg="#28a745", fg="#fff", command=calculate_sqrt).grid(row=r, column=c, pady=5)
    else:
        tk.Button(root, text=button_text, padx=38, pady=20, font=("Arial", 14), bg="#6c757d", fg="#fff", command=lambda text=button_text: add_to_entry(text)).grid(row=r, column=c, pady=5)
        
root.mainloop()
