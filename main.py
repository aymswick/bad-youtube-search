#Bad Youtube Search - Python 3
from tkinter import *



def onClick():
    print("Hello")

#Run this on application create
app = Tk()
app.title("Bad Youtube Search")
app.geometry("600x400")
app.configure(bg="#8f8f8f")

#Input Box
entryBox = Entry(app, font=("Roboto", 24), fg="#5e5e5e", justify="center" )

#Send Button
sendButton = Button(app, font="Roboto", text="Search", width="300", height=5,
                    bd=0, bg="#c0392b", fg="#ffffff", activeforeground="#ffffff" ,activebackground="#e74c3c", justify="center",
                    command=onClick)
entryBox.place(x=55, y=100, height=50, width=500)
sendButton.place(x=155, y=175, height=50, width=300)

app.mainloop()
