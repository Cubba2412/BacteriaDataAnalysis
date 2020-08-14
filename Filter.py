from PrintAndUserInput import inputChoiceNum, printBacteriaType

def dataFilter(data, bacteria, l_lim, u_lim):
    # DATAFILTER Filters the given data for chosen conditions, 
    # returns an updated set of data, wherein all data 
    # complies with the given conditions.
    #
    # Usage: data  = filter(data, bacteria, l_lim, u_lim)
    #
    # Input: data (matrix of floats), bacteria (integer), 
    #           l_lim (integer), u_lim (integer)
    # Output: data (matrix of floats)
    #
    # Author: Casper Grindsted, s183688@student.dtu.dk, 2020
    
    #Filter for specific type of bacteria
    if (bacteria != 0):
        data = data[data[:,2] == bacteria] #Update data to only contain chosen type of bacteria 
    
    #Filter for a desired interval for growth rate
    if ((l_lim != 0) or (u_lim != 0)):
        data = (data[data[:,1] >= l_lim]) #Update data with a lower limt for growth rate
        data = (data[data[:,1] <= u_lim]) #Update data with a upper limt for growth rate
        
    
    return data


def filterChoice(bacteria, l_lim, u_lim, dataFiltered):
    # FILTERCHOICE Prompts the user for a choice of filter, 
    # returns the choices as well as a flag indicating the data is to be filtered 
    ##
    # Usage: bacteria, l_lim, u_lim, dataFiltered = filterChoice(dataFiltered)
    ##
    # Input: bacteria (integer), l_lim (integer), u_lim (integer)
    #        dataFiltered (Boolean)
    # Output: same as input
    ##
    # Author: Thomas B. Frederiksen, s183729@student.dtu.dk, 2020
    while True:
        try:
            if(dataFiltered):
                choice = inputChoiceNum("\n Would you like to clear previous filters? (Y:1, N:0)", "Y/N")
                if (choice):
                    l_lim = 0
                    u_lim = 0
                    bacteria = 0
                    dataClear = True
                    dataFiltered = False
                else:
                    break
            else:
                choice = inputChoiceNum("Would you like to filter for bacteria? (Y:1, N:0) ", "Y/N")
                if (choice):
                    printBacteriaType()
                    bacteria = inputChoiceNum("Please enter a Bacteria Type: ", "Bacteria")
                    dataFiltered = True
                else:
                    bacteria = 0
                choice = inputChoiceNum("Would you like to set a lower and upper limit? (Y:1, N:0) ", "Y/N")
                if (choice):
                    l_lim = inputChoiceNum("Please enter a lower limit for the growth rate: ", "Limit")
                    u_lim = inputChoiceNum("Please enter a upper limit for the growth rate: ", "Limit")
                    dataFiltered = True
                    break
                elif(bacteria == 0) and not (choice):
                    choice = inputChoiceNum("So you don't want to set any filters? (Y:1, N:0) ", "Y/N")
                    if(choice == 1):
                        pass
                    else:
                        print("\nReverting to main menu...")
                        if(dataClear):
                            l_lim = 0
                            u_lim = 1
                            bacteria = 0
                        break
                else:
                    l_lim = 0
                    u_lim = 1
                    break
            
        except:
            print("\n Error whiel choosing filter type")
            pass
    
    return bacteria, l_lim, u_lim, dataFiltered
