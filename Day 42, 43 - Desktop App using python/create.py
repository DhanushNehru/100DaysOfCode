# !/usr/bin/python3
import tkinter
from PIL import ImageTk, Image as image

window = tkinter.Tk()
window.title("Dhanush Desktop App")
window.configure(bg="#db7c23")
window.iconbitmap('DN.ico')
window.geometry("500x500")


    
# picture = tkinter.PhotoImage(file="Instagram.png")

# pic = tkinter.Label(window, image=picture)
# pic.pack(pady=10)


# picture = ImageTk.PhotoImage(file="Instagram.jpg")

# picture2 = image.open("Instagram.jpg")
# pic_resized = picture2.resize((350,450), image.ANTIALIAS)

# picture3 = ImageTk.PhotoImage(pic_resized)


# lab = tkinter.Label(window, image = picture3, width=200, height=400)
# lab.pack()

# close = tkinter.Button(window, text="close", command=window.destroy)
# close.pack()


def click():
    var = entry.get()
    label1 = tkinter.Label(window, text =var, font="<> 10", padx=50, pady=10)
    label1.pack(pady=25)
    entry.delete(0,'end')

label = tkinter.Label(window, text = " How are you today ? ", 
    bg="#0a8ca6",
    fg="#8c180b", 
    font="<> 20",
    pady=30,
    padx=10
    )

label.pack()

entry = tkinter.Entry(window, w=30, font="none 20")
# entry.insert(0, 'Type here ...')
entry.pack(pady=10)



button = tkinter.Button(window, text=" Submit ",
    bg="#99803c",
    fg="#1c1606", 
    font="android 20",
    padx=30,
    pady=15,
    command= click
)
button.pack()

window.mainloop()