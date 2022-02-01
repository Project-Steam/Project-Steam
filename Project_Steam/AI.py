import json

def swap(lst, x, y):
    global swap1, swap2
    swap1 = x
    swap2 = y

    lst[x], lst[y] = lst[y], lst[x]


def partition(arr, start, end):
    global i
    global pivotind

    pivotind = end
    pivot = arr[pivotind]
    i = start - 1

    for j in range(start, end):
        if letterwaarde(arr[j], pivot):
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, end)
    return i + 1


def quicksort(arr, start, end):
    if len(arr) == 1:
        return

    if end > start:
        pivot = partition(arr, start, end)

        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)


def letterwaarde(woord1, woord2):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", ]
    woord1 = woord1.lower()
    woord2 = woord2.lower()

    if len(woord1) == 0 or len(woord2) == 0:
        return True

    if woord1.lower() == woord2.lower():
        return True

    i = 0
    for letter in woord1.lower():
        if letter not in alphabet:
            continue

        while woord2[i] not in alphabet:
            if len(woord2[i:]) == 1:
                return False
            i += 1

        if alphabet.index(letter) < alphabet.index(woord2[i]):
            return True

        if alphabet.index(letter) == alphabet.index(woord2[i]):
            return letterwaarde(woord1[1:], woord2[1:])

        return False


def quicksortcaller(arr):
    quicksort(arr, 0, len(arr) - 1)


def allgameslength():
    with open("sortedgames.txt", "r") as f:
        return len(f.readlines())

def hatedgame():
    max = [0, "game"]
    steam_files = open('steam.json')
    data = json.load(steam_files)
    for game in data:
        if game['negative_ratings'] > max[0]:
            max[0] = game['negative_ratings']
            max[1] = game['name']

    return max


def lovedgame():
    max = [0, "game"]
    steam_files = open('steam.json')
    data = json.load(steam_files)
    for game in data:
        if game['positive_ratings'] > max[0]:
            max[0] = game['positive_ratings']
            max[1] = game['name']

    return max


def mostplayedgame():
    played = [0, "game"]
    steam_files = open('steam.json')
    data = json.load(steam_files)
    for game in data:
        owners = game["owners"].split("-")
        owners = int(owners[1]) + int(owners[0]) / 2
        playtime = int(game['average_playtime'])
        if playtime * owners > played[0]:
            played[0] = int(playtime * owners)
            played[1] = game['name']

    return played


def leastplayedgame():
    played = [99999999, "game"]
    steam_files = open('steam.json')
    data = json.load(steam_files)
    for game in data:
        owners = game["owners"].split("-")
        owners = int(owners[1]) + int(owners[0]) / 2
        playtime = int(game['average_playtime'])
        if playtime * owners < played[0]:
            played[0] = int(playtime * owners)
            played[1] = game['name']

    return played


def mostexpensivegame():
    max = [0, "game"]
    steam_files = open('steam.json')
    data = json.load(steam_files)
    for game in data:
        if game['price'] > max[0]:
            max[0] = game['price']
            max[1] = game['name']

    return max