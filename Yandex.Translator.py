try:
    with open("secretKey.txt", "r") as f:
        secretKey = f.read()
except FileNotFoundError:
    print("SecretKey file required to run this app, or you can run it with variable secretKey equals your yandex.translate secretKey")
import sys
import tkinter as tk
import tkinter.font as font
from yandex.Translater import Translater as Translater
import requests
import webbrowser
import re

#import multiprocessing
class translatin:
    def __init__(self):
        self.times = 1
        
    def translate(self, text, lanFrom, lanTo):
        if self.times != 0:
            tr = Translater()
            tr.set_key(secretKey)
            if re.search(r'[А-я]', text):
                tr.set_from_lang('ru')
                tr.set_to_lang('en')
            else:
                tr.set_from_lang('en')
                tr.set_to_lang('ru')
            if text != "":
                tr.set_text(text)
                textboxR.delete('1.0', "end-1c")
                textboxR.insert("1.0", tr.translate())
            
        self.times += 1            
def openYandex(*args):
    webbrowser.open("https://translate.yandex.ru", new=0)

#When we press any button, there starts a funcion, checking if something changed from previous check. Interval = 800 in TK
prev = ""

def getUpdates():
    global prev
    current = textboxL.get("1.0", "end-1c")
    if prev != current:
        trObject.translate(current, "en", "ru")
        prev = current
    if current == "":
        textboxR.delete('1.0', "end-1c")
    textboxL.after(800, getUpdates)


depth=0
root = tk.Tk()

tk.Label(root, text="From").grid(row=0, column=0)
tk.Label(root, text="To").grid(row=0, column=2)


root.title("Translator")
textboxL = tk.Text(root, height=12 , width=30, highlightbackground = "#e5e5e5", highlightcolor= "#ffdc61")
textboxL['font'] = font.Font(size=15, family="Roboto", weight="bold")
textboxL.grid(row=1, column=0, padx=(25, 10))

textboxR = tk.Text(root, height=12, width=30, highlightbackground = "#e5e5e5", highlightcolor= "#ffdc61")
textboxR['font'] = font.Font(size=15, family="Roboto", weight="bold")
textboxR.grid(row=1, column=2, padx=(25, 10))
trObject = translatin()
getUpdates()

#This line is required for yandex translate usage 
link = tk.Label(root, text="Powered by Yandex.Translate", fg="#daa520", cursor="hand2")
link.grid(row=4, column=1)
link.bind("<Button-1>", openYandex)


tk.mainloop()
