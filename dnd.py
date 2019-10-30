#!/usr/bin/python
import os
import time
import json
import random


#Vars
#global gamedata
    #gamedata = dnd

#global itemdata
#    itemdata = gamedata/itemdat/

#global playersheet
#    playersheet = gamedata/Playerdat/

global player


def init():
    #BANNER HERE
    #global player
    os.system('clear')
    print("-----------------------")
    print("DnD Managment script")

    print("-----------------------")
    print("")
    print("Please choose a charicter sheet")
    print("-------------------------------")
    #os.system('ls Playerdat')
    lst = []
    for x in lst:
        print(x)
    ans = input()
    if ans == 1:
        print(" ")
    time.sleep(3)
    menu()


def menu():
    os.system('clear')
    print("-----------------------")
    print("DnD Managment script")
    print("-----------------------")
    print("Please make a selection")
    print("1.   Show skills")
    print("2.   Show Inventory")
    print("3.   Roll Dice")
    print("99.  Quit")
    ans = input()
    if ans == "1":
        showskills()
    elif ans == "2":
        showinv()
    elif ans == "3":
        roll()
    elif ans == "99":
        os.system('clear')
        quit()


def showskills():
    os.system('clear')
    print("|--------------|")
    print("|Showing Skills|")
    print("|--------------|")
    print("")
    # TODO: Add a checker to make sure they didnt over stack
    #maybe use a key validation system to make sure people dont cheat
    time.sleep(5)
    menu()


def showinv():
    os.system('clear')
    print("|-----------------|")
    print("|Showing Inventory|")
    print("|-----------------|")
    print("")
    time.sleep(5)
    menu()


def roll():
    os.system('clear')
    print("|-------------------|")
    print("|Please select a die|")
    print("|-------------------|")
    print("")
    print("1.   20d")
    print("2.   6d")
    print("99.  Main Menu")
    #make a roll animation
    ans = input()
    if ans == "1":
        x = random.randint(1, 20)
    elif ans == "2":
        x = random.randint(1, 6)
    elif ans == "99":
        menu()
    # TODO: add a condidtion, if 20 then x = NAT 20 !!
    print("")
    print("|-------------------|")
    print("|Your roll:" + str(x))
    print("|-------------------|")
    if x == "20":
        print("!! NAT 20 !!")
    time.sleep(2)
    roll()


menu()
