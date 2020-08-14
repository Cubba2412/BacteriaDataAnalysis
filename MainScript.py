  # MAINMENU Main script to run the bacterial analysis program utilizing 
  #          the functions of the other files imported from the same directory
  ##
  # Usage: mainMenu()
  ##
  # Author: Thomas B. Frederiksen, s183729@student.dtu.dk, 2020

import os.path
folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)
from DataStatistics import dataStatistics, printStatOptions
from dataLoad import dataLoad
from PrintAndUserInput import *
from DataPlotFunktion import *
from Filter import *

def mainMenu():
    #Initiliaze variables
    print("Welcome to the python Bacteria Data Analysis program")
    dataLoaded = False
    dataFiltered = False
    dataChoice = 1
    dataNotLoaded = "Data has not been loaded. Please load data to perform calculations"
    bacteriaTypes = {1:'Salmonella enterica', 2: 'Bacillus cereus', 3: 'Listeria', 4: 'Brochothrix thermosphacta'}
    while True:
        try:
            printMenu()
            #If the data has been filtered, inform the user
            if(dataFiltered):
                print("\n\nFiltered data available")
                print("Current data filter parameters: ")
                print("Bacteria Type:",bacteriaTypes[bacteria])
                print("Lower and Upper limit [{:.2f}, {:.2f}]".format(l_lim,u_lim))
            
            #Prompt user for a menu choice, and act upon the choice
            choice = inputChoiceNum("Please choose an option: ", "Menu")            
            if(choice == 1):
                while True:
                    try:
                        #Load datafile if it is a valid filename, otherwise
                        #reprompt for valid filename
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
                #If data has not been loaded, inform the user load data
                if not(dataLoaded):
                    print(dataNotLoaded)
                else:
                    while True:
                       try:
                           #Prompt the user for the type of filter they want
                           bacteria, l_lim, u_lim, dataFiltered = filterChoice(dataFiltered) 
                           newDat = dataFilter(data,bacteria,l_lim,u_lim)
                           break
                       except ValueError:
                           print("Error when filtering the data")
                           pass  
                       
            elif(choice == 3):
                #If data has not been loaded, inform the user load data
               if not(dataLoaded):
                    print(dataNotLoaded)
               else:
                   while True:
                       try:
                           #Present statistical calculation options
                           print("\nStatistical calculation options: ")
                           printStatOptions()
                           #Prompt if the calculation should be based on the 
                           #original or filtered data
                           if(dataFiltered):
                               dataChoice = inputChoiceNum("Would you like to calculate statistics of the original data (1) or the filtered data (2): ", "Filtered data")
                           statisticChoice = inputChoiceStr("Please enter a statistic to calculate: ")
                           #Calculate statistic
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
                   #Present statistic calculated
                   print(statType,statistic, "\n")
            elif(choice == 4):
                #If data has not been loaded, inform the user load data
                if not(dataLoaded):
                    print(dataNotLoaded)
                elif(dataFiltered):
                    while True:
                       try:       
                           #Prompt if the plot should be generated from the 
                           #original or filtered data
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
                    
            #Exit the program, by breaking the loop
            elif(choice == 5):
                print("Goodbye")
                break
        except:
            pass
    return 

#Run the main script
mainMenu()
    
