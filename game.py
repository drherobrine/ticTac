import random #Note:  the table looks like this: 0   1   2
import time   #                                  3   4   5
import sys    #                                  6   7   8

number = 27
playerNumber = 25


moveMemory = [0, 1, 2, 3, 4, 5, 6, 7, 8]
blackList = ["asd", 23]

move = False

class Slot():

    _isOccupied = False
    _isCross = False
    _isCircle = False

    def __init__(self, isOccupied, isCross, isCircle):
        self._isOccupied = isOccupied
        self._isCross = isCross
        self._isCircle = isCircle

    def isSlotOccupied(self):
        if self._isOccupied == True:
            return self._isOccupied

    def isSlotCross(self):
        if self._isCross == True:
            self._isOccupied = True
            return self._isCross

    def isSlotCircle(self):
        if self._isCircle == True:
            self._isOccupied = True
            return self._isCircle


instances = [Slot(False, False, False), Slot(False, False, False), Slot(False, False, False), Slot(False, False, False), Slot(False, False, False), "x3y2", "x1y3", "x2y3", "x3y3"]
for i in range(0,9):
    instances[i] = Slot(False, False, False)

players = ["Player"]
starter = random.choice(players)

print("Principles of the game: . = unoccupied, X = occupied by You, O = occupied by CPU.")
print("%s begins!"%starter)

def winCheck():
    #Check Horizontal wins
    if (instances[0]._isCross and instances[1]._isCross and instances[2]._isCross) or (instances[3]._isCross and instances[4]._isCross and instances[5]._isCross) or (instances[6]._isCross and instances[7]._isCross and instances[8]._isCross):
        print("You won!")
        return "win"
    #Check for Vertical wins
    elif (instances[0]._isCross and instances[3]._isCross and instances[6]._isCross) or (instances[1]._isCross and instances[4]._isCross and instances[7]._isCross) or (instances[2]._isCross and instances[5]._isCross and instances[8]._isCross):
        print("You won!")
        return "win"
    #Check for diagonal wins
    elif (instances[0]._isCross and instances[4]._isCross and instances[8]._isCross) or (instances[2]._isCross and instances[4]._isCross and instances[6]._isCross):
        print("You won!")
        return "win"


    # Check Horizontal losses
    if (instances[0]._isCircle and instances[1]._isCircle and instances[2]._isCircle) or (instances[3]._isCircle and instances[4]._isCircle and instances[5]._isCircle) or instances[6]._isCircle and (instances[7]._isCircle and instances[8]._isCircle):
        print("You lost. :(")
        return "win"
    # Check for Vertical losses
    elif (instances[0]._isCircle and instances[3]._isCircle and instances[6]._isCircle) or (instances[1]._isCircle and instances[4]._isCircle and instances[7]._isCircle) or (instances[2]._isCircle and instances[5]._isCircle and instances[8]._isCircle):
        print("You lost. :(")
        return "win"
    # Check for diagonal losses
    elif (instances[0]._isCircle and instances[4]._isCircle and instances[8]._isCircle) or (instances[2]._isCircle and instances[4]._isCircle and instances[6]._isCircle):
        print("You lost miserably. :(")
        return "win"


def cpuMove():
    for i in range(0,9):
        if instances[i]._isOccupied == False:
            sys.stdout.write(".   ")
        elif instances[i]._isCross == True:
            sys.stdout.write("X   ")
        elif instances[i]._isCircle == True:
            sys.stdout.write("O   ")
        else:
            sys.stdout.write("????")
        if i == 2 or i == 5 or i == 8:
            print("\n")
    number = 23
    while number in blackList:
        number = random.choice(moveMemory)
    blackList.append(number)
    instances[number]._isCircle = True
    instances[number]._isOccupied = True


def plrMove():
    print("\nYour turn!")
    for i in range(0,9):
        if instances[i]._isOccupied == False:
            sys.stdout.write(".   ")
        elif instances[i]._isCross == True:
            sys.stdout.write("X   ")
        elif instances[i]._isCircle == True:
            sys.stdout.write("O   ")
        else:
            sys.stdout.write("Err ")
        if i == 2 or i == 5 or i == 8:
            print("\n")
    while playerNumber in blackList:
        playerNumber = 1
        playerNumber = int(input("Type your move here(" + str(moveMemory) + "):"))
    blackList.append(playerNumber)
    print(playerNumber)
    instances[playerNumber].isCross = True
    instances[playerNumber].isOccupied = True




while True:
    for i in range(0,9):
        if instances[i]._isOccupied == False:
            sys.stdout.write(".   ")
        elif instances[i]._isCross == True:
            sys.stdout.write("X   ")
        elif instances[i]._isCircle == True:
            sys.stdout.write("O   ")
        else:
            sys.stdout.write("Err ")
        if i == 2 or i == 5 or i == 8:
            print("\n")
    if starter == "Player":
        playerNumber = int(input("Type your move here("+str(moveMemory)+"):"))
        instances[playerNumber]._isCross = True
        instances[playerNumber]._isOccupied = True
        move = False

    if move == False:
        print("CPU's turn!")
        cpuMove()
        move = True
    else:
        print("Your Turn!")
        plrMove()
        move = False
    didWin = winCheck()

    if didWin == "win":
        break
    else:
        pass

#dasdasdasdsd

