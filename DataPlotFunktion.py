
import numpy as np
import matplotlib.pyplot as plt 

def dataPlot(data):
    # DATAPLOT Plots the given data in two charts.
    #
    # Usage: data  = dataPlot(data)
    #
    # Input: data (matrix of floats)
    # Output: Column chart and growth rate chart
    #
    # Author: Casper Grindsted, s183688@student.dtu.dk, 2020
   
    #Seperate data according to the number(1, 2, 3, 4) defined in the 3th column of input: data 
    #Data for datatype 1
    x1 = data[data[:,2]==1, 0]
    y1 = data[data[:,2]==1, 1]
    
    #Data for datatype 2
    x2 = data[data[:,2]==2, 0]
    y2 = data[data[:,2]==2, 1]
    
    #Data for datatype 3
    x3 = data[data[:,2]==3, 0]
    y3 = data[data[:,2]==3, 1]
    
    #Data for datatype 4
    x4 = data[data[:,2]==4, 0]
    y4 = data[data[:,2]==4, 1]
    
    #Arrange data from smallest to largest
    sort1 = np.argsort(x1)
    sort2 = np.argsort(x2)
    sort3 = np.argsort(x3)
    sort4 = np.argsort(x4)
    
    
    #Bar chart
    x = ['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta'] #Each category of bacteria
    if (len(x1) != 0):                      #Check if data exist, if it doesn't dont plot
        plt.bar(x[0], len(x1), color="b")
    if (len(x2) != 0):
        plt.bar(x[1], len(x2), color="b")
    if (len(x3) != 0):
        plt.bar(x[2], len(x3), color="b")
    if (len(x4) != 0):
        plt.bar(x[3], len(x4), color="b")
    plt.title("Number of bacteria")         #Set the title of the graph
    #plt.xlabel("Data")                     #Set the x-axis label
    plt.ylabel("Amount of bacteria")        #Set the y-axis label
    plt.xticks(rotation=15)                 #Rotate labels to avoid overlap
    plt.show()

    
    #Growth rate chart
    if (len(x1) != 0):                      #Check if data exist, if it doesn't dont plot
        plt.plot(x1[sort1], y1[sort1], "r", label='Salmonella enterica') #Plot line graph of data
        plt.plot(x1, y1, "ro")              #Plot scatter plot of data
    if (len(x2 != 0)):                                       
        plt.plot(x2[sort2], y2[sort2], "b", label='Bacillus cereus')
        plt.plot(x2, y2, "bo") 
    if (len(x3 != 0)): 
        plt.plot(x3[sort3], y3[sort3], "y", label='Listeria')
        plt.plot(x3, y3, "yo") 
    if (len(x4 != 0)): 
        plt.plot(x4[sort4], y4[sort4], "g", label='Brochothrix thermosphacta')
        plt.plot(x4, y4, "go")
    plt.title("Growth rate by temperature") #Set the title of the graph
    plt.xlabel("Temperature")               #Set the x-axis label
    plt.ylabel("Growth rate")               #Set the y-axis label
    plt.xlim([10, 60])                      #Set the limits of the x-axis
    plt.ylim([0, 1])                        #Set the limits of the y-axis
    plt.grid(color='black', linestyle='--', linewidth=0.2) #Plot grid
    plt.legend(loc="best")                  #Place legend where minimum overlap with data occurs
    plt.show()    
    
    return


