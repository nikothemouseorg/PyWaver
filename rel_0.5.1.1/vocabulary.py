from math import floor
from random import randint
from defWaves import *
t = True
yes = ["yes", "y", "1"]
no = ["no", "n", "0"]

selExit = ["4", "e", "exit"]

selCombine = ["1", "c", "combine"]

newWave = [0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, ]


waves = ["Saw", "DblSaw", "Square", "Square37p5", "Square25", "Square12p5", "Sine", "Triangle"]

def generate():
    for i6 in range(0, 64):
        add2 = randint(0, 63)
        newWave[i6] = add2
        i6 += 1
    print(newWave[0], newWave[1], newWave[2], newWave[3], newWave[4], newWave[5], newWave[6], newWave[7], newWave[8],
          newWave[9], newWave[10], newWave[11], newWave[12], newWave[13], newWave[14], newWave[15], newWave[16],
          newWave[17], newWave[18], newWave[19], newWave[20], newWave[21], newWave[22], newWave[23], newWave[24],
          newWave[25], newWave[26], newWave[27], newWave[28], newWave[29], newWave[30], newWave[31], newWave[32],
          newWave[33], newWave[34], newWave[35], newWave[36], newWave[37], newWave[38], newWave[39], newWave[40],
          newWave[41], newWave[42], newWave[43], newWave[44], newWave[45], newWave[46], newWave[47], newWave[48],
          newWave[49], newWave[50], newWave[51], newWave[52], newWave[53], newWave[54], newWave[55], newWave[56],
          newWave[57], newWave[58], newWave[59], newWave[60], newWave[61], newWave[62], newWave[63])
    print("Here you go, a fresh new generated wave!")


def combine(wv1, wv1amp, wv2, wv2amp, amp, centered):
    midVal = 0
    if wv1 == waves[6]:
        wv1 = Sine
    if wv2 == waves[6]:
        wv2 = Sine
    if wv1 == waves[7]:
        wv1 = Triangle
    if wv2 == waves[7]:
        wv2 = Triangle
    if wv1 == waves[0]:
        wv1 = Saw
    if wv2 == waves[0]:
        wv2 = Saw
    if wv1 == waves[1]:
        wv1 = DblSaw
    if wv2 == waves[1]:
        wv2 = DblSaw
    if wv1 == waves[2]:
        wv1 = Square
    if wv2 == waves[2]:
        wv2 = Square
    if wv1 == waves[3]:
        wv1 = Square37p5
    if wv2 == waves[3]:
        wv2 = Square37p5
    if wv1 == waves[4]:
        wv1 = Square25
    if wv2 == waves[4]:
        wv2 = Square25
    if wv1 == waves[5]:
        wv1 = Square12p5
    if wv2 == waves[5]:
        wv2 = Square12p5
    if amp == "":
        amp = 1
    for i11 in range(0, len(wv1)):
        wv1[i11] = floor(wv1[i11] * wv1amp)
    for i12 in range(0, len(wv2)):
        wv2[i12] = floor(wv2[i12] * wv2amp)
    for i5 in range(0, 64):
        preadd = wv1[i5] + wv2[i5]
        add = floor(preadd / 2)
        newWave[i5] = floor(add * amp)
        print(add)
        newWave[i5] = floor(newWave[i5] * amp)
    if centered == 1:
        for i13 in range(0, len(newWave)):
            midVal = midVal + newWave[i13]
        midVal = floor(midVal / (2 * len(newWave)))
    print(newWave[0],  newWave[1], newWave[2],  newWave[3], newWave[4],  newWave[5], newWave[6],  newWave[7],
          newWave[8],  newWave[9], newWave[10],  newWave[11], newWave[12],  newWave[13], newWave[14],  newWave[15],
          newWave[16],  newWave[17], newWave[18],  newWave[19], newWave[20],  newWave[21], newWave[22],  newWave[23],
          newWave[24],  newWave[25], newWave[26],  newWave[27], newWave[28],  newWave[29], newWave[30],  newWave[31],
          newWave[32],  newWave[33], newWave[34],  newWave[35], newWave[36],  newWave[37], newWave[38],  newWave[39],
          newWave[40],  newWave[41], newWave[42],  newWave[43], newWave[44],  newWave[45], newWave[46],  newWave[47],
          newWave[48],  newWave[49], newWave[50],  newWave[51], newWave[52],  newWave[53], newWave[54],  newWave[55],
          newWave[56],  newWave[57], newWave[58],  newWave[59], newWave[60],  newWave[61], newWave[62],  newWave[63])
    print(f"{midVal} is middle")
    print("Here you go, a neat combination!")


def waitselection():
    sel = input("Selection: ")
    while t:
        for i1 in range(0, 3):
            if sel == selCombine[i1]:
                print("Please select which waves you'd like to combine.\nAvailable:\nSine\nTriangle\nSaw")
                print("Square\n Square 37.5: Square37p5\nSquare 25: Square25\nSquare 12.5: Square12p5")
                print("Double-Sided Saw: DblSaw")
                print("(For technical reasons Dbl-Sided Saw is 1 octave higher than other waveforms.)")
                wave1 = input("Selection: ")
                print("Please select which waves you'd like to combine.\nAvailable:\nSine\nTriangle\nSaw")
                print("Square\n Square 37.5: Square37p5\nSquare 25: Square25\nSquare 12.5: Square12p5")
                print("Double-Sided Saw: DblSaw")
                wave2 = input("Selection 2: ")
                for i9 in range(0, 8):
                    if wave1 == waves[i9]:
                        break
                    else:
                        wave1 = "Sine"
                for i10 in range(0, 8):
                    if wave2 == waves[i10]:
                        break
                    else:
                        wave2 = "Sine"
                combine(wave1[0], wave2[0])


combine(Square, 1, DblSaw, 1, 3, 1)
