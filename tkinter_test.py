from tkinter.ttk import *

from tkinter import Tk, PhotoImage
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("布局管理 place")
root["bg"] = "white"

style_default = Style()

style_default.configure("TLabel", foreground="red", background="white")

def on_onclick():
    ret = messagebox.askquestion("tialsdf", 'asdfaf')
    print('ret=',ret)

file = PhotoImage(file="hh.png")
button = Button(root, text="与那阿斯蒂芬", image=file,width=100, style="TLabel",command=lambda : messagebox.askquestion("title", "message"))
button.pack(pady=10)
entry =Entry(root)
entry.pack(pady=10)
root.mainloop()
