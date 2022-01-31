from tkinter import *
import json
from tkcalendar import Calendar
from tkinter import *

time_hour = []
minutes_time = []
list_of_game_names = []


def start_up():
    # Time
    for i in range(24):
        time_hour.append('{:02}'.format(i))

    for i in range(00, 60, 15):
        minutes_time.append('{:02}'.format(i))

    # Game_list
    steam_files = open('steam.json')
    data = json.load(steam_files)

    for i in data:
        list_of_game_names.append(i['name'])
    list_of_game_names.sort()


def create_main_menu():
    root = Tk()
    root.title('Dashboard')

    window_width = 500
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Set main menu in the middle of screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Create a button to open menu
    calendar_button = Button(text='Plan a game session', command=lambda: create_calander())
    calendar_button.pack(expand=True)

    friend_group = Button(text='Create friend group')
    friend_group.pack(expand=True)

    favorite_games = Button(text='Select and view favorite games')
    favorite_games.pack(expand=True)

    root.mainloop()


def create_calander():
    root = Tk()
    root.title('Create a play session')

    window_width = 625
    window_height = 625

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Set menu in the middle of screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Add Calendar
    global cal
    cal = Calendar(root, selectmode='day',
                   year=2022, month=1,
                   day=14, date_pattern='dd/mm/y')

    cal.pack(pady=20)

    # Add Buttons and Labels

    # Sessions
    make_session_button = Button(root, text="Make session",
                                 command=make_session, activebackground='green')
    make_session_button.pack()
    make_session_button.place(y=500, x=300)

    see_session_button = Button(root, text="See sessions",
                                command=see_sessions, activebackground='green')
    see_session_button.pack(side='left')
    see_session_button.place(y=500)

    planned_sessions_label = Label(root, text="Planned sessions: ")
    planned_sessions_label.pack(side='left')
    planned_sessions_label.place(y=350)

    # Time
    global hour_time
    hour_time = StringVar(root)
    hour_time.set(time_hour[0])

    global time_minutes
    time_minutes = StringVar(root)
    time_minutes.set(minutes_time[0])

    hour_choice = OptionMenu(root, hour_time, *time_hour)
    hour_choice.pack(side='left')
    hour_choice.place(y=245, x=100)

    minute_choice = OptionMenu(root, time_minutes, *minutes_time)
    minute_choice.pack(side='left')
    minute_choice.place(y=245, x=150)

    time_label = Label(root, text='Select a time: ')
    time_label.pack(side='left')
    time_label.pack()
    time_label.place(y=250)

    # Friends
    global friend_name
    friend_name = StringVar(root)
    friend_name.set(steam_friends[0])

    friend_choice = OptionMenu(root, friend_name, *steam_friends)
    friend_choice.pack(side='left')
    friend_choice.place(y=280, x=50)

    friend_label = Label(root, text='Friend: ')
    friend_label.pack(side='left')
    friend_label.pack()
    friend_label.place(y=285)

    # Games
    global game_name
    select_games_label = Label(root, text="Select a game: ")
    select_games_label.pack(side='left')
    select_games_label.place(y=320)

    game_name = StringVar(root)
    game_name.set(list_of_game_names[0])

    game_choice = OptionMenu(root, game_name, *list_of_game_names)
    game_choice.pack(side='left')
    game_choice.place(y=315, x=100)

    # Show sessions
    global text_widget
    text_widget = Text(root, height=5, width=75)
    text_widget.pack(side='left')
    scrollbar = Scrollbar(root).pack(side='right')
    root.mainloop()


def make_session():
    save_info = f'{cal.get_date()} with {friend_name.get()} at {hour_time.get()}:{time_minutes.get()} to play:{game_name.get()}\n'
    with open('dates.txt', 'a') as outfile:
        outfile.write(save_info)


def see_sessions():
    text_widget.delete('1.0', END)
    print(f'All the sessions on {cal.get_date()}')
    file = open('dates.txt', 'r')
    lines = file.readlines()

    for i in lines:
        i.strip()
        lines.sort()
        text_widget.insert(INSERT, i)
    file.close()

def get_steam_friends():
    friend_steam_ids = []
    for i in range(11):
         friend_steam_ids.append(i)
    return friend_steam_ids


steam_friends = get_steam_friends()
start_up()
create_main_menu()
