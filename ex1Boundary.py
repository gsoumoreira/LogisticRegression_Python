# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:58:41 2019

@author: gabi
"""

def exBound(theta_0,theta_1,theta_2,hip):

    import numpy as np
    import random
    import matplotlib.pyplot as plt
    
    # Making the limited random samples
    x1 = np.linspace(-15,-7,20)
    y1 = np.linspace(2,10,20)
    ex_point_x1 = random.choices(x1,k=20)
    ex_point_y1 = random.choices(y1,k=20)

    x2 = np.linspace(-6,2,20)
    y2 = np.linspace(11,18,20)
    ex_point_x2 = random.choices(x2,k=20)
    ex_point_y2 = random.choices(y2,k=20)

    # Creating a Figure obect (dpi changes the basic unit size)
    fig = plt.figure(figsize=(12,6))
    fig.patch.set_facecolor('xkcd:white')

    # Settubg axis position and size
    axes = fig.add_axes([0,0,1,1])
    axes.set_facecolor('lightyellow')
    
    # Inserting grid on the figure
    axes.grid(b=True, which='major', axis='both', linestyle='-', linewidth=0.5)
    axes.minorticks_on()
    axes.grid(b=True, which='minor', axis='both', linestyle=':',linewidth=0.2)

    
    # Plotting the samples
    axes.plot(ex_point_x1,ex_point_y1,'r',linewidth=0, linestyle='-',alpha=1,
                  marker='o', markersize=10, markeredgewidth=1)
    axes.plot(ex_point_x2,ex_point_y2,'b',linewidth=0, linestyle='-',alpha=1,
                  marker='o', markersize=10, markeredgewidth=1)

    # Starting the linear boundary model
    num_points = 20
    x_0 = np.array([1]*num_points)
    x_1 = np.array(list(range(0,num_points)))
    
    # Computing linear boundary conditions
    x_2= (- (x_0*theta_0) - (x_1*theta_1) + hip)/theta_2
    
    # Plot the linear boundary
    axes.plot(x_2,x_1)
    
    return axes
