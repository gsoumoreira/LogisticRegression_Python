#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:40:10 2018

Sigmoid function 

@author: gabi (based on ML Coursera Course)
"""

import numpy as np # Library dedictated to vectorial math


# Defining a function using Python

def sigmoid(z):
    
    g = 1/(1+(np.exp(-z)))
    
    return g

