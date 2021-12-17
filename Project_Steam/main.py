from tkinter import *
from tkinter.messagebox import showinfo

def hoofdscherm():
    root = Tk()

    label = Label(master=root, text='STEAM Dashboard Groep 1', height=2)
    label.pack(fill="both", expand=True)

    button1 = Button(master=root, text='Login', command=login)
    button1.pack(pady=10)

    button2 = Button(master=root, text='Games', command=games)
    button2.pack(pady=10)

    button3 = Button(master=root, text='Exit', command=exit)
    button3.pack(pady=10)
    #entry = Entry(master=root)
    #entry.pack(padx=10, pady=10)

    root.mainloop()
    return

def login():
    print("test login")
    return

def games():
    print("test games")
    return

def exit():
    print("test logout")
    return

hoofdscherm()