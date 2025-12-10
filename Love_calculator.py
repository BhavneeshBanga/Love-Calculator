import tkinter as tk
from tkinter import ttk
import random

from PIL import Image, ImageTk

numbers = '123456789'

root = tk.Tk()
root.geometry('400x300')
root.title('LOVE CALCULATOR')

path = "love.png"
load = Image.open(path)
render = ImageTk.PhotoImage(load)
root.iconphoto(False, render)

name_label = ttk.Label(root, text='Your Name:')
name_label.pack(pady=3)

name_entry = ttk.Entry(root)
name_entry.pack(pady=5)
name_entry.focus()


email_label = ttk.Label(root, text='Partner Name:')
email_label.pack(pady=2)


email_entry = ttk.Entry(root)
email_entry.pack(pady=5)
# def Lovepercentage():
def greet():
    name = name_entry.get()
    greeting_label.config(text=(random.choices(numbers)+random.choices(numbers)))

greet_button = tk.Button(root, text="Find Love Percentage", command=greet)
greet_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()