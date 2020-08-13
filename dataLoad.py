# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:51:48 2020

@author: ThomasBirk
"""

import numpy as np

def dataLoad(filename):
    # DATALOAD Loads in a text data containing N x 3 data values and
    # returns it as a float array
    ##
    #Usage: data = dataLoad(filename)
    ##
    #Input filename: filename of textfile (String of full path to file)
    # Output data: N x 3 float array with the data contained 
    # in the text file given
    ##
    #Author: Thomas B. Frederiksen s183729@student.dtu.dk, 2020
    
    filein = open(filename, "r") # Opens the file for reading
    lines = filein.readlines() # Reads all lines into an array
    #Initialize variables
    count = 0 
    data = np.empty([0,3])
    #Find number of lines
    count = len(lines)    
    #Filter for invalid data rows, and save valid rows in float array
    for i in range(0,count):
            if not(10 <= float(lines[i].split()[0]) <= 60):
                print("WARNING: The observation in row {:d} was removed as it was below 10 or above 60 degrees".format(i))
                pass
            if not(float(lines[i].split()[1]) > 0):
                print("WARNING: The observation in row {:d} was removed as the growth rate was negative".format(i))
                pass
            if not(1 <= int(lines[i].split()[2]) <= 4):
                print("WARNING: The observation in row {:d} was removed as it did not match the bacteria type code".format(i))
                pass
            else:
                data = np.vstack((data,lines[i].split())) 
    return data.astype(np.float)


Data = dataLoad('test.txt')

