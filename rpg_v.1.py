# Name: Rolando Holmes
# date: 2017 April 27
# description: Text-based RPG

import random
import time


def theIntro():
    print("Coming home after a long days work, you are exhausted.")
    time.sleep(3)
    print("you make your way up the driveway to your house, looking forward to a relaxing evening.")
    time.sleep(3)
    print("But before you relax for the day you have two thoughts in your head")
    time.sleep(3)


def choiceMade():
    choice = ""
    while choice != "1" and choice != "2":  # input validation
        choice = input("Should I go and get food or Stay and check the kitchen? (1 or 2):  ")
    return choice


def checkChoice(choiceMade):
    correctChoice =(1, 2)

    if choiceMade == str("1"):
        print("You decided to stay, but as you walk up to the front door")
        time.sleep(3)
        print("You find it cracked open...")
    elif choiceMade == str("2"):
        print("You leave to get food, but for some strange reason")
        time.sleep(3)
        print("walking up to your door, there was an uneasy feeling...of all the days.")

#Branching path if player chooses 1

def chapterOne_B1():
    print("Almost regretting your decision to investigate you realize that")
    time.sleep(3)
    print("There seems to be a sign of struggle, why is this you ask?")
    time.sleep(3)
    print("Looking around your demolished house, it seems whoever 'they' were")
    time.sleep(3)
    print("did not find what they were looking for, and you also notice blood spots.")
    time.sleep(3)
    print("The blood looks to be a broken trail.")
    time.sleep(3)

def choiceMade_B1():
    choiceB1 = ""
    while choiceB1 !="1" and choiceB1 != "2":
        choiceB1 = input("You ask yourself outloud, should I follow it or call the cops? (1 or 2): ")
        return choiceB1

def checkChoice_B1(choiceMade_B1):
    correctChoice_B1 = (1,2)
    if choiceMade_B1 == str ("1"):
        print("Following the blood trail, you hope you can handle whats at the end")
        time.sleep(3)
        print("You see it leads back outside. now you wonder, did i pass them already?")
        time.sleep(3)
        print("Gathering your thoughts you can't think why blood would lead back out")
        time.sleep(3)
        print("On top of that you think why did you not notice it before?")
    elif choiceMade_B1() == str ("2"):
        print("You call the cops, sadly you are put on  hold")
        time.sleep(3)
        print("constantly pacing you think should I go get them personally?")
        time.sleep(3)
        print("But you also think that if you leave 'they' could come back")
        time.sleep(3)
        print(" Finally!!! you are put through to an officer")


 #Branching path if player chooses 2

def chapterOne_B2():
    print("Ignoring that un-settling feeling deep down")
    time.sleep(3)
    print("You head out to a fast food resturant to eat.")
    time.sleep(3)
    print("As you order, you realized your wallet is at home!")
    time.sleep(3)
    print("What will you do?")

def choiceMade_B2(): #Branching story #1
    choiceB2 = ""
    while choiceB2 !="1" and choiceB2 !="2":
        choiceB2 = input("I just going to call it a night or think up somthing! (1 or 2): ")
        return choiceB2

def checkChoice_B2(choiceMade_B2):
    correctChoice_B2 = (1,2)
    if choiceMade_B2 == str ("1"):
        print("You head home pissed and hungry...")
        time.sleep(3)
        print("But the anger subsides, and turns into a panic, as you find")
        time.sleep(3)
        print("Your house broken into")

    elif choiceMade_B2 == str ("2"):
        print("You hurry and look for money in your car")
        time.sleep(3)
        print("Drive thru traffic is backed up but moving slowly.")
        time.sleep(3)
        print("To your surprise you actually find moeny")
        time.sleep(3)
        print("No question")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    theIntro()
    check = choiceMade()
    checkChoice(check)  # check is equal to "1" or "2"
    chapterOne_B1()
    check_B1 = choiceMade_B1()
    checkChoice_B1(check_B1)
    chapterOne_B2()
    check_B2 = choiceMade_B2()
    checkChoice_B2(check_B2)
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")