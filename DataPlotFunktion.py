# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 09:56:37 2020

@author: cgrin

Data plot funktion
"""

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
   
    print("Generating plots...")
    #Seperate data according to the number(1, 2, 3, 4) defined in the 3th column of input: data 
    #Data for datatype 1
    ind1 = data[data[:,2]==1]
    x1 = ind1[:,0]
    y1 = ind1[:,1]
    
    #Data for datatype 2
    ind2 = data[data[:,2]==2]
    x2 = ind2[:,0]
    y2 = ind2[:,1]
    
    #Data for datatype 3
    ind3 = data[data[:,2]==3]
    x3 = ind3[:,0]
    y3 = ind3[:,1]
    
    #Data for datatype 4
    ind4 = data[data[:,2]==4]
    x4 = ind4[:,0]
    y4 = ind4[:,1]
    
    
    
    #Column chart
    bar_data = np.array([len(x1), len(x2), len(x3), len(x4)]) #Amount of each bacteria
    leg = ['1', '2', '3', '4']              #Legend name
    leg_pos = np.arange(len(leg))           #Legend position
    plt.bar(leg_pos, bar_data, color="b")   #Plot bar chart
    plt.xticks(leg_pos, leg)                #Plot legend
    plt.title("Number of bacteria")         #Set the title of the graph
    plt.xlabel("Data")                      #Set the x-axis label
    plt.ylabel("Amount of bacteria")        #Set the y-axis label
    plt.show()
    
    #Growth rate chart
    #x = np.array([-3, -1, 0, 3, 3])        #Temp (1st column )
    #y = np.array([0, -2, 0, -1, 2])        #Growth (2nd column )
    plt.plot(x1, y1, "ro", label='1')       #Plot line graph of x and y
    plt.plot(x2, y2, "bo", label='2')       #Scatter plot with blue stars
    plt.plot(x3, y3, "yo", label='3')       #Plot line graph of x and y
    plt.plot(x4, y4, "go", label='4')
    plt.title("“Growth rate by temperature")#Set the title of the graph
    plt.xlabel("Temperature")               #Set the x-axis label
    plt.ylabel("Growth rate")               #Set the y-axis label
    plt.xlim([10, 60])                      #Set the limits of the x-axis
    plt.ylim([0, 1])                       #Set the limits of the y-axis
    plt.grid(color='black', linestyle='--', linewidth=0.2) #Plot grid
    plt.legend(loc="best")                  #Place legend where minimum overlap with data occurs
    plt.show()    
    
    return