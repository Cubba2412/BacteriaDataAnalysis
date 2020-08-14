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
import os.path

def mainMenu():
    
    print("Welcome to the python Bacteria Data Analysis program")
    dataLoaded = False
    dataFiltered = False
    dataNotLoaded = "Data has not been loaded. Please load data to perform calculations"
    bacteriaTypes = {1:'Salmonella enterica', 2: 'Bacillus cereus', 3: 'Listeria', 4: 'Brochothrix thermosphacta'}
    while True:
        try:
            printMenu()
            if(dataFiltered):
                print("\n\nFiltered data available")
                print("Current data filter parameters: ")
                print("Bacteria Type:",bacteriaTypes[bacteria])
                print("Lower and Upper limit [{:.2f}, {:.2f}]".format(l_lim,u_lim))
                
            choice = inputChoiceNum("Please choose an option: ", "Menu")            
            if(choice == 1):
                while True:
                    try:                        
                        filename = inputChoiceStr("Please enter the name of the datafile to load: ")
                        if(os.path.isfile(filename)):
                            data = dataLoad(filename)
                            dataLoaded = True
                            break
                        else:
                            print("\nFile not found. Please enter valid filename")
                    except:
                        print("\nError while loading datafile")
                           
            elif(choice == 2):
                if not(dataLoaded):
                    print(dataNotLoaded)
                else:
                    while True:
                       try:
                           bacteria, l_lim, u_lim, dataFiltered = filterChoice(dataFiltered) 
                           newDat = dataFilter(data,bacteria,l_lim,u_lim)
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
                           print("\nCalculation options: ")
                           printStatOptions()
                           if(dataFiltered):
                               dataChoice = inputChoiceNum("Would you like to calculate statistics of the original data (1) or the filtered data (2): ", "Filtered data")
                           statisticChoice = inputChoiceStr("Please enter a statistic to calculate: ")
                           if(dataChoice == 2):
                               statType,statistic = dataStatistics(newDat,statisticChoice)
                               break
                           else:
                               statType,statistic = dataStatistics(data,statisticChoice)
                               break
                           if(statistic == "Error"):
                              raise ValueError()
                           else:
                               break
                       except ValueError:
                           print("\nStatistic not found \nPlease enter one of the following valid statistics: \n")
                           
                           pass
                   print(statType,statistic, "\n")
            elif(choice == 4):
                if not(dataLoaded):
                    print(dataNotLoaded)
                elif(dataFiltered):
                    while True:
                       try:        
                           dataChoice = inputChoiceNum("Would you like to plot the original data (1) or the filtered data (2): ", "Filtered data")
                           if(dataChoice == 2):
                               dataPlot(newDat)
                               break
                           else:
                               dataPlot(data)
                               break
                       except ValueError:
                           print("Error when creating plots")
                           pass
                else:
                    dataPlot(data)
                    
            elif(choice == 5):
                print("Goodbye")
                break
        except:
            pass
    return 

mainMenu()
    
