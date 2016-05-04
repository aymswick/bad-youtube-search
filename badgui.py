from Tkinter import *
from main import *

def searchButtonClicked(event):
    youtube_search(entryBox.get())

#Run this on application create
app = Tk()
app.title("Bad Youtube Search")
app.geometry("600x400")
app.configure(bg="#8f8f8f")

#Input Box
entryBox = Entry(app, font=("Roboto", 24), fg="#5e5e5e", justify="center" )
#Auto focus input box
entryBox.focus()

#Send Button
sendButton = Button(app, font="Roboto", text="Search", width="300", height=5,
                    bd=0, bg="#c0392b", fg="#ffffff", activeforeground="#ffffff" ,activebackground="#e74c3c", justify="center",
                    command= lambda: searchButtonClicked(1))
entryBox.place(x=55, y=100, height=50, width=500)

sendButton.place(x=155, y=175, height=50, width=300)

#Send input on enter/return key press
app.bind('<Return>', searchButtonClicked)

app.mainloop()
