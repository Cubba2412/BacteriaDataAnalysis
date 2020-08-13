# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:16:34 2020

@author: ThomasBirk
"""
from DataStatistics import dataStatistics, printStatOptions
from dataLoad import dataLoad
from PrintAndUserInput import *
from DataPlotFunktion import *
from Filter import *

def mainMenu():
    
    print("Welcome to the python Bacteria Data Analysis program")
    dataLoaded = False
    dataNotLoaded = "Data has not been loaded. Please load data to perform calculations"
    while True:
        try:
            printMenu()
            choice = inputChoiceMenuNum("Please choose an option: ")
            
            
            if(choice == 1):
                filename = inputChoiceStr("Please enter the name of the datafile to load: ")
                data = dataLoad(filename)
                dataLoaded = True
                dataTmp = data # Keep original data by only performing calculations a seperate variable
            elif(choice == 2):
                if not(dataLoaded):
                    print(dataNotLoaded)
                else:
                    while True:
                       try:        
                           Bacteria = inputChoiceBac("Please enter a Bacteria Type: ")
                           l_lim = inputChoiceLim("Please enter a lower limit for the growth rate")
                           u_lim = inputChoiceLim("Please enter a upper limit for the growth rate")
                           newDat = dataFilter(dataTmp,bacteria,l_lim,u_lim)
                           if(newDat == data):
                               raise ValueError()
                           else:     
                               print(newDat)
                               break
                       except ValueError:
                           print("Error when filtering the data")
                           pass   
            elif(choice == 3):
               if not(dataLoaded):
                    print(dataNotLoaded)
               else:
                   while True:
                       try:        
                           statisticChoice = inputChoiceStr("Please enter a statistic to calculate: ")
                           statType,statistic = dataStatistics(dataTmp,statisticChoice)
                           if(statistic == "Error"):
                              raise ValueError()
                           else:
                               break
                  
                       except ValueError:
                           print("\nStatistic not found \nPlease enter one of the following valid statistics: \n")
                           printStatOptions()
                           pass
                       
                   print(statType,statistic, "\n")
            elif(choice == 4):
                if not(dataLoaded):
                    print(dataNotLoaded)
                else:
                     dataPlot(data)
            elif(choice == 5):
                print("Goodbye")
                break
        except:
            pass
    return 
    
