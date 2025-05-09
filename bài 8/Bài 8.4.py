print(" Thai Van Ngoc")
print("MSSV:235752020710016 ")
print("#####################")
from tkinter import *
window = Tk()
window.title("Welcome to LikeGreeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)
window.mainloop()
    
