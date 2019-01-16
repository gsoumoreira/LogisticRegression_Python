#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:26:13 2018

This file contains code for the ex1 - linear regression exercise in pyhton.
It will cover the following parts:
    
   1 - WarmUpExercise - Importing files in python
   2 - Importing dataset Organazing Data
   3 - Plotting the data (data presentation)
   4 - Gradiente descent and compute cost function for one feature
   5 - Estimate the profit for different values
   6 - Linear Regression plot
   7 - Cost Function plot with different theta values
   

The ex1_Data.txt contains information about population size in different 
citties (First column - numbers in 10.000s) and the profit of the company in
these citties (Second column - numbers in 10.000)

@author: gabi
"""

#%% Part 1 - Importing the indenMatrix() function from warmUpExercise.py file

# import warmUpExercise as wue

# A = wue.idenMatrix() # A will receive the 2D 5x5 array identity

#%%  Part 2 - Importing and Organazing Data

import numpy as np
import pandas as pd

# Path for data file
pathtodata = 'Exercise_Data/ex1_Data.txt'

# Importing data using Pandas (Importing as DataFrame
data = pd.read_csv(pathtodata,delimiter = ',',header=None)

# Selecting the column variable with the profits 
y = data[[2]]

# Number of training examples 
m = len(y) 

# Adding a new column to the dataset with ones values
data["ones"] = np.ones(m)

# Choose the header feature index
data.columns = ['X1','X2','X3','X0']

# Selecting the column variable with the population of citties 
popci = pd.DataFrame(data.iloc[:,0])

#%% Part 3 - Plotting the Exercising Data

# MLplot source code for details
import MLplot as pl

pl.plot2D(popci,y)

#%% Part 4 - Cost funtion and gradient descent for one feature

# Setting the Features for linear regression
x = data.loc[:,['X0','X1']]

# Important gradient descent variables
iterations = 1500 # Number of iterations
alpha = 0.01 # Learning rate

# Initialize fitting parameters 
theta0 = pd.DataFrame([0,0])

# Compute and display initial cost (Choosing theta0)
import computeCost as cc

J = cc.computeCost(x,y,theta0)

# Gradient Descent, Cost Function History and Theta History
import gradientDescent as gd

[bestHip,Jhist,thetahist] = gd.gradientDescent(x,y,theta0,alpha,iterations)

#%% Part 5 - Estimate the profit for different x values

predict1 = np.dot(np.transpose(pd.DataFrame([1, 3.5])),bestHip)
predict2 = np.dot(np.transpose(pd.DataFrame([1,7])),bestHip)

#%% Part 6 - Plotting the Linear Regression

# Check the MLplot source code for regressionPlot details
regplot = pl.regressionPlot(x,y,bestHip,1)

# Setting the title and axis label
regplot.set_title('Linear Regression')
regplot.set_xlabel('Population in 10.000s')
regplot.set_ylabel('Profit in $10.000s')

#%% Part 7 - Cost Function plot with different theta values

# Setting theta_0 and theta_1 variation values
test = pl.plot2D(thetahist[[1]],Jhist)