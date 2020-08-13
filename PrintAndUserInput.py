# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:06:55 2020

@author: ThomasBirk
"""

def dataNotLoaded():
    print("Data has not been loaded. Please load data to perform calculations")
    return


def printMenu():
    
    
    print("\n1. Indlæs data.")
    print("2. Filtrer data.")
    print("3. Vis statistik.")
    print("4. Generer diagrammer.")
    print("5. Afslut.")
    
    return

def inputChoiceMenuNum(prompt):
    # INPUTNUMBER Prompts user to input a number
    
    while True:
        try:
            num = int(input(prompt))
            if not(0 < num < 6):
                pass
                print("Please enter a number between 1 and 5")
            else:
                break
        except ValueError:
            pass
            print("Please enter a number between 1 and 5")
    return num

def inputChoiceLim(prompt):
    # INPUTNUMBER Prompts user to input a number
    
    while True:
        try:
            num = float(input(prompt))
            if not(0 <= num <= 1):
                pass
                print("Please enter a decimal number between 0 and 1")
            else:
                break
        except ValueError:
            pass
            print("Please enter a decimal number between 0 and 1")
    return num


def inputChoiceBac(prompt):
    # INPUTNUMBER Prompts user to input a number
    
    while True:
        try:
            num = int(input(prompt))
            if not(0 < num < 5):
                pass
                print("Please enter a number between 1 and 4")
            else:
                break
        except ValueError:
            pass
            print("Please enter a number between 1 and 4")
    return num

def inputChoiceStr(prompt):
    # INPUTNUMBER Prompts user to input a number
    
    while True:
        try:
            string = input(prompt)
            if string.isdigit():
                pass
                print("Please enter a valid string")
            else:
                break
        except ValueError:
            pass
    return string