# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 11:06:55 2020

@author: ThomasBirk
"""

def printMenu():
    
    print("\n1. Load data.")
    print("2. Filter data.")
    print("3. Display statistics.")
    print("4. Generate plots.")
    print("5. Quit.")
    
    return

def printBacteriaType():
    print("\nPlease Choose a bacteria")
    print("1 Salmonella enterica")
    print("2 Bacillus cereus")
    print("3 Listeria")
    print("4 Brochothrix thermosphacta")
    return

def inputChoiceNum(prompt, inputType):
    # INPUTNUMBER Prompts user to input a number
    
    while True:
        try:
            if (inputType == "Limit"):
                num = float(input(prompt))
            else:
                num = int(input(prompt))
            if not(0 < num < 6) and (inputType == "Menu"):
                pass
                print("Please enter a number between 1 and 5")
            elif not(0 < num < 5) and (inputType == "Bacteria"):
                pass
                print("Please enter a number between 1 and 4")
            elif not(0 <= num <= 1) and (inputType == "Y/N"):
                pass
                print("Please enter a valid option (No: 0, Yes: 1) ")
            elif not(0<= num <=1) and (inputType == "Limit"):
                pass
                print("Please enter a valid growth rate limit (between 0 and 1)")
            elif not(1<= num <=2) and (inputType == "Filtered data"):
                pass
                print("Please enter a valid plot option: \n1: Plot original data \n2: Plot Filtered data")
            else:
                break
        except ValueError:
            pass
            print("Please enter a number")
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