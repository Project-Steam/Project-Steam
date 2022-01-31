import random
from tkinter import *
from threading import *


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

