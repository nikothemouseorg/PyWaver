from vocabulary import *
t = True
f = False


def exit():
    print("Bro you sure? [Y/N]")
    while t:
        isExit = str(input())
        for i in range(0, 11):
            if isExit == yes[i]:
                print("Ok, bye.")
                quit()
            i += 1
        else:
            print("Invalid. Valid values: Y/N/0/1")


def waitSelection(sel):
    if sel == 1:
        print("What waveforms would you like to combine?")





