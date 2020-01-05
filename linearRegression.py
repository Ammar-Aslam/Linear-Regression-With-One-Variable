# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:07:53 2018

@author: Ammar
"""

import csv

import matplotlib.pyplot
import pylab
import numpy as np



#Reading the file 
with open('ex1data1.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)


#Separating the data in two lists of Profit and Population

Profit=[]
Population=[]

for i in range(len(data)):
    Profit.append(float(data[i][1]))
    Population.append(float(data[i][0]))



#Suppose initially theeta0=0.5 and theeta 1=0.5
    
theeta0=0.5
theeta1=0.5




#function to update values of theeta0
def updateTheeta0(m,theeta0,theeta1,Population = [],Profit=[]):
    alpha=0.005
    sum=0
   
    for i in range(len(Population)):
        term1=theeta0+theeta1*Population[i]
        term2=term1-Profit[i]
        sum=sum+term2
    cost=alpha*(sum/m)
    return (theeta0-cost)

#function to update values of theeta1
def updateTheeta1(m,theeta0,theeta1,Population = [],Profit=[]):
    alpha=0.005
    sum=0
   
    for i in range(len(Population)):
        term1=theeta0+theeta1*Population[i]
        term2=Population[i]*(term1-Profit[i])
        sum=sum+term2
    cost=alpha*(sum/m)
    return (theeta1-cost)

    


#Running 1000 iterations to update theeta values
for i in range(0, 1000):

    tempTheeta0=updateTheeta0(len(Population),theeta0,theeta1,Population,Profit)
    tempTheeta1=updateTheeta1(len(Population),theeta0,theeta1,Population,Profit)
    theeta0=tempTheeta0
    theeta1=tempTheeta1

#printing final weights   
print("Final Weights")    
print("-------------------") 
print("Theeta0:")
print(theeta0)
print("Theeta1:")
print(theeta1)    

#printing scatter plot of data as well as the line produced by our weights

matplotlib.pyplot.scatter(Population,Profit)
matplotlib.pyplot.xlabel("Population of City in 10,000s")
matplotlib.pyplot.ylabel("Profit in $10,000s")



y_points=[]
for i in range(len(Population)):
    y_points.append(theeta0+theeta1*Population[i])

matplotlib.pyplot.plot(Population,y_points,"r-")
#matplotlib.pyplot.plot(np.unique(Population), np.poly1d(np.polyfit(Population, Profit, 1))(np.unique(Population)),"b-")
matplotlib.pyplot.show()






