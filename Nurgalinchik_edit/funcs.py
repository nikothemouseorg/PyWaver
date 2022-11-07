from vocabulary import *

username = ""
if username == "":
    print("Please, introduce yourself: ")
    username = input()
    print("Ok!")


def menu():
    print(f"Welcome, {username}!")
    print("                  ---+++===   MENU   ===+++---                  ")
    print("1: Combine Waveform")
    print("2: Create Waveform")
    print("3: Info/Help")
    print("4: Exit")
    waitselection()