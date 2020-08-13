

import numpy as np



#This function calculates the statistic given a keyword
#
# Usage: data = statistic
#
# Input Data(Nx3 Matrix of the data) Statistic(Array of strings)
# Output result(float)
#
# Author: Henrik Riise Nieslen  S183693


#The matrix is divided into: Temperature, Growth rate, Bacteria
#This function calculates the statistic given a keyword
def dataStatistics(data, statistic):
    
    statistic=statistic.lower()
    statType =""

    
    if statistic == "mean temperature":
        result = np.mean(data[:,0])                             #Takes the mean value of coloumn 0
        statType="Mean Temperature: "
        
        
    elif statistic == "mean growth rate":
        result = np.mean(data[:,1])                             #Takes The mean value of coloumn 1
        statType="Mean Growth rate: "
        
        
    elif statistic == "std temperature":
        result = np.std(data[:,0])                              #Finds the standard deviation of coloumn 0
        statType="Std Temperature: "
        
        
    elif statistic == "std growth rate":
        result = np.std(data[:,1])                              #Finds the standard deviation of coloumn 1
        statType="Std Growth rate: "
        
        
    elif statistic == "rows":
        result = len(data)                                      #Finds how many rows are in the matrix
        statType="Number of Rows: "

        
        
    elif statistic == "mean cold growth rate":
        x=0
        while True:
            try:
                if data[x][0] > 20: #checks if the row has the the target temperature
                    data = np.delete(data, (x), axis=0) #deletes the current row
                    x=x-1
                x=x+1
            except IndexError:
                break
        result = np.mean(data[:,1])     #Takes the mean value of coloumn 1 where the temperature is less than 20
        statType="Mean Cold Growth rate: "
        
        
    elif statistic == "mean hot growth rate":
        x=0
        while True:
            try:
                if data[x][0] < 50: #checks if the row has the the target temperature
                    data = np.delete(data, (x), axis=0) #deletes the current row
                    x=x-1
                x=x+1
            except IndexError:
                break
            result = np.mean(data[:,1])     #Takes the mean value of coloumn 1 where the temperature is more than 50
            statType="Mean Hot Growth rate: "
            
        
    else:
        result = "Error"
    
    return statType, result



#This function prints the differnt options that the user can choose between
#
# Usage: print(options
#
# Input nan
# Output nan
#
# Author: Henrik Riise Nieslen  S183693
def printStatOptions():
    
    options = (np.array(["Mean Temperature", "Mean Growth rate", "Std Temperature",
                "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]))
    print(*options, sep="\n")   #prints the array in a list seperated by new lines
    
    return    



print(dataStatistics(np.array([[11, 2,  3],
                               [20, 5,  6],
                               [50, 8,  9],
                               [35, 11,12],
                               [11, 12, 3],
                               [20, 7,  6],
                               [50, 18, 9],
                               [35, 11,12]]), "Mean hot growth rate"))









