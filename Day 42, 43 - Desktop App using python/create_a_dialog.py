# !/usr/bin/python3
import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image as image


window = tkinter.Tk()
window.title("Dhanush Desktop App")
window.configure(bg="#263d42")
window.iconbitmap('DN.ico')
window.geometry("400x500")

def openpic():
    window.filename = filedialog.askopenfilename(title="Open picture", 
    filetypes=(("png file","*.png"), ("jpg file","*.jpg")))
    picture = image.open(window.filename)
    pic_resized = picture.resize((400,450), image.ANTIALIAS)
    new = ImageTk.PhotoImage(pic_resized)
    lab = tkinter.Label(frame, image=new)
    lab.pack()




open = tkinter.Button(window, text="Open", padx=40, pady=10, command=openpic)
frame = tkinter.Frame(window, width=400, height=450, bg="#263d42")

frame.pack()
open.pack()

window.mainloop()