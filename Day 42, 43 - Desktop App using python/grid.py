# !/usr/bin/python3
import tkinter

window = tkinter.Tk()
window.title("Dhanush Desktop App")
window.configure(bg="#263d42")
window.iconbitmap('DN.ico')
window.geometry("300x400")



def p():
    t = box.get()
    global lab
    lab = tkinter.Label(window, text=t)
    lab.grid(row=3, column = 0, columnspan=2, pady=10)

def c():
    lab.destroy()


text = tkinter.Label(window, text="Enter text", font="none 15",
    padx=10,
    pady=10,
    bg="#263d42",
    fg="white"
)

box = tkinter.Entry(window, font="none 15", w=20)

print = tkinter.Button(window, text='PRINT',font="none 15", padx=30, pady=10, command=p)
clear = tkinter.Button(window, text='CLEAR',font="none 15", padx=30, pady=10, command=c)

text.grid(row=0, column=0, padx=10, pady=10)
box.grid(row=0, column=1, padx=10,pady=10 )
print.grid(row=1,column=0, columnspan=2, pady=10)
clear.grid(row=2, column=0, columnspan=2)

window.mainloop()