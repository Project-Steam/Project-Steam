from tkinter import *
import json
from tkinter.messagebox import showinfo

def hoofdscherm():
    root = Tk()
    root.title('Steam Dashboard')

    label = Label(master=root, text='STEAM Groep 1', height=2)
    label.pack(fill="both", expand=True)

    login_button = Button(master=root, text='Login', command=login)
    login_button.pack(pady=10)

    game_button = Button(master=root, text='Games', command=games)
    game_button.pack(pady=10)

    lijstspel_button = Button(master=root, text='lijst', command=newwindow)
    lijstspel_button.pack(pady=10)

    exit_button = Button(master=root, text='Exit', command=root.destroy)
    exit_button.pack(pady=10)
    #entry = Entry(master=root)
    #entry.pack(padx=10, pady=10)

    root.mainloop()
    return

def login():
    print("test login")
    return

def games():
    print("test games")
    # Load Json file
    steam_files = open('steam.json')
    data = json.load(steam_files)
    list_of_game_names = []

    # Get every item in data
    for i in data:
        list_of_game_names.append(i['name'])

    return newwindow(list_of_game_names)


def newwindow(game_names):
    # Sort the list of game names
    game_names.sort()


    root = Tk()
    root.title('Steam gamelist')

    scroll = Scrollbar(master=root)
    scroll.pack(side = RIGHT)

    game_name_label = Label(master=root, text=game_names, height=2)
    game_name_label.pack(fill="both", expand=True)

    return

hoofdscherm()