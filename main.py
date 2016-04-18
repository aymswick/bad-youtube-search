#Bad Youtube Search - Python 3
from tkinter import *



def onClick():
    print("Hello")

#Run this on application create
app = Tk()
app.title("Bad Youtube Search")
app.geometry("600x400")
app.configure(bg="#8f8f8f")

#Send Button
sendButton = Button(app, font="Helvetica", text="SEND", width="50", height=5,
                    bd=0, bg="#BDE096", activebackground="#BDE096", justify="center",
                    command=onClick)

sendButton.place(x=255, y=360, height=40, width=130)

app.mainloop()
