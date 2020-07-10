import random
import sys
import enchant
import threading

set1 = set()

def removeHint():
    print(end="\r")
    print ("Done")


def randLetter():
    a = random.choice("qwertyuiopasdfghjklzxcvbnm")
    return a


def checkWord(a, b):
    if b.startswith(a):
        return True
    else:
        return False


def givePoints(a):
    return len(a)


def dupliCheck(m):
    if m in set1:
        print("Already entered")
        return False
    else:
        set1.add(m)
        return True


def userCommand(a):
    if a == "show points":
        print("Player 1 has ", s1, " points")
        print("Player 2 has ", s2, " points")
        return True
    if a == "end":
        if s1 > s2:
            print("Congrats, player 1 has won the game with ", s1 - s2, " points more")
            sys.exit("Thanks for playing")
            return True
        else:
            print("Congrats, player 2 has won the game with ", s2 - s1, " points more")
            sys.exit("Thanks for playing")
            return True
    if a == "Help":
        print("Type show points to view scores")
        print("Type end to finish game")

        print("Make word from ending letter of previous word, no duplicate words allowed")
def startGame():
    d2 = enchant.DictWithPWL("en_US", "mywords.txt")
    print("Welcome to world build!")
    print("Type out 'end' to end game")
    print("Type out show points to show points")
    letter = randLetter()
    print("Your first letter is ", letter)
    x = 1
    p1 = ""
    p2 = ""
    global s1
    s1 = 0
    global s2
    s2 = 0
    while x > 0:
        p1 = input("Player1 enter a string")
        while userCommand(p1):
            p1 = input("Player1 enter a string")
        if checkWord(letter, p1) and dupliCheck(p1):
            if d2.check(p1):
                print("Valid word")
                s1 = s1 + givePoints(p1)
                print(givePoints(p1), " points added")
                letter = p1[-1]
            else:
                print("No points added")
                print("Word does not exist in the Oxford Dictionary")
                timer = threading.Timer(5.0, removeHint)
                print("Press enter key after the hint")
                timer.start()
        else:
            print("No points added")
            print("Make word from letter ", letter)

        www=input(d2.suggest(p1))
        p2 = input("Player2 enter a string")
        while userCommand(p2):
            p2 = input("Player2 enter a string")
        if checkWord(letter, p2) and dupliCheck(p2):
            if d2.check(p2):
                print("Valid word")
                s2 = s2 + givePoints(p2)
                print(givePoints(p2), " points added")
                letter = p2[-1]
            else:
                print("No points added")
                print("Word does not exist in the Oxford Dictionary")
        else:
            print("No points added")
            print("Make word from letter ", letter)
        x = x + 1


startGame()