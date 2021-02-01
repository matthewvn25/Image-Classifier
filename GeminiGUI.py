#import tkinter
#from tkinter import *

from PIL import Image, ImageTk

import tkinter as tk
window = tk.Tk()

load = Image.open("background.jpg")
render = ImageTk.PhotoImage(load)

label = tk.Label(image=render)
label.image = render
label.place(x=0, y=0)


window.wm_title("Gemini Scrapper - Find your perfect Waifu")
window.geometry("500x500")

button = tk.Button(text ="Click!",width = 5, height =1)
button.pack()

entry = tk.Entry()
entry.pack()

window.mainloop()
