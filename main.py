#Bad Youtube Search - Python 3
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.goButton = Button(self, fg="red", bg="blue")
        self.goButton["text"] = "Huh?"
        self.goButton["command"] = self.yell
        self.goButton.pack(side="top")

        self.QUIT = Button(self, text="QUIT", fg="red",
                           command=app.destroy)
        self.QUIT.pack(side="bottom")

    def yell(self):
        print("AHHHHHHHHHHHHHHHHH")

#Run this on application create
app = Tk()
app.title("Bad Youtube Search")
app.geometry("600x400")
app.configure(bg="#8f8f8f")
app.mainloop()
