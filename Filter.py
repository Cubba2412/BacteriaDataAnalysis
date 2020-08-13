# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:29:00 2020

@author: cgrin

Filter
"""

import numpy as np

def dataFilter(data, bacteria, l_lim, u_lim):
    # FILTER Filters the given data for chosen conditions, 
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