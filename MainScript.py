# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:16:34 2020

@author: ThomasBirk
"""
from DataStatistics import dataStatistics, printStatOptions
from dataLoad import dataLoad

def mainMenu():
    
    welcomeMessage()
    
    while True:
        try:
            printMenu()
            choice = inputChoiceNum("Please choose an option: ")
            
            
            if(choice == 1):
                filename = inputChoiceStr("Please enter the name of the datafile to load: ")
                data = dataLoad(filename)
                dataLoaded = True
                dataTmp = data # Keep original data by only performing calculations a seperate variable
            elif(choice == 2):
                if not(dataLoaded):
                   dataNotLoaded()
                else:
                    x = 1   
            elif(choice == 3):
               if not(dataLoaded):
                   dataNotLoaded()
               else:
                   while True:
                       try:        
                           statisticChoice = inputChoiceStr("Please enter a statistic to calculate: ")
                           statistic = dataStatistics(dataTmp,statisticChoice)
                           if(statistic == "Error"):
                              raise ValueError()
                           else:
                               break
                  
                       except ValueError:
                           print("\nStatistic not found \nPlease enter one of the following valid statistics: \n")
                           printStatOptions()
                           pass
                       
                   print(statistic, "\n")
            elif(choice == 4):
                if not(dataLoaded):
                   dataNotLoaded()
                else:
                     x = 1
               # dataPlot()
            elif(choice == 5):
                print("Goodbye")
                break
        except:
            pass
    return choice

def welcomeMessage():
    print("Welcome to the python Bacteria Data Analysis program")
    return
    
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

def inputChoiceNum(prompt):
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