import tkinter as tk
import random
import string
import pyperclip
from tkinter import PhotoImage
import webbrowser
from PIL import Image
import csv
import os
import sys

def generate_password():
    length = spinbox.get()
    if int(length) > 33:
        length = 32
    if int(length) < 7:
        length = 8
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    copy_to_clipboard = clipboard_var.get()
    csv_file = csv_file_var.get()
    info_clip_label.config(text="")
    info_csv_label.config(text="")
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = random.sample(characters,int(length))
    password_string = "".join(password)
    password_label.config(text=password_string, font=("Arial", 10))
    if copy_to_clipboard:
        pyperclip.copy(password_string)
        info_clip_label.config(text="Password copied to clipboard", font=("Arial", 8))

    if csv_file:
        with open("passwords.csv", "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([password_string])
            info_csv_label.config(text="Password saved to CSV file", font=("Arial", 8))

def open_github(event):
    webbrowser.open("https://github.com/ekomlenovic/password_generator")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.title("Password Generator")
root.wm_title("Password Generator")
root.resizable(False, False)
root.iconbitmap(resource_path("data/DALL_E_preview.ico"))

# Length label and spinbox
length_label = tk.Label(root, text="Password Length:(8-32)")
length_label.grid(row=0, column=0)

spinbox = tk.Spinbox(root, from_=8, to=32, width=5, value = 12)
spinbox.grid(row=0, column=1)

# Checkboxes for character types
uppercase_var = tk.IntVar()
uppercase_var.set(1)
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0)

lowercase_var = tk.IntVar()
lowercase_var.set(1)
lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=1)

numbers_var = tk.IntVar()
numbers_var.set(1)
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0)

symbols_var = tk.IntVar()
symbols_var.set(1)
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=1)

clipboard_var = tk.IntVar()
clipboard_var.set(1)
clipboard_checkbox = tk.Checkbutton(root, text="Copy to Clipboard", variable=clipboard_var)
clipboard_checkbox.grid(row=3, column=0)

csv_file_var = tk.IntVar()
csv_file_var.set(1)
csv_file_checkbox = tk.Checkbutton(root, text="Save to CSV file", variable=csv_file_var)
csv_file_checkbox.grid(row=3, column=1)

# Generate password button and password label
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="")
password_label.grid(row=5, column=0, columnspan=2)


info_clip_label = tk.Label(root, text="")
info_clip_label.grid(row=6, column=0, columnspan=2)

info_csv_label = tk.Label(root, text="")
info_csv_label.grid(row=7, column=0, columnspan=2)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(row=8, column=0, columnspan=2)

# Load Github logo and create label
path = resource_path("data/github-mark.png")
logo = PhotoImage(file=path)
logo = logo.subsample(8, 8)
github_label = tk.Label(root, image=logo)
github_label.grid(row=9, column=0, columnspan=2, pady=10)
github_label.bind("<Button-1>", open_github)

root.mainloop()
