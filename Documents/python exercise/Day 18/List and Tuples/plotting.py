# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:32:24 2020

@author: Mahendra
"""


import matplotlib.pyplot as plt


"""
1. Five data points...(x,y)...(0,0),
(1,3),(2,1),(3,5),(4,2)
"""
# def main():
#     x_cor = [0,1,2,3,4]
#     y_cor = [0,3,1,5,2]
    
#     # Plot..
#     plt.plot(x_cor,y_cor)
    
#     # Display the line graph
#     plt.show()
    
# main()

# def main():
#     x_cor = [0,1,2,3,4]
#     y_cor = [0,3,1,5,2]
    
#     # Plot..
#     plt.plot(x_cor,y_cor)
    
#     #Add a title
    
#     plt.title("Test Plot")
    
#     # Add labels to the plot
#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")
    
#     # Add a grid
#     plt.grid(True)
    
#     # Display the line graph
#     plt.show()
    
# main()


# def main():
#     x_cor = [0,1,2,3,4,3,6,7,8,9,10]
#     y_cor = [0,3,1,5,2,4,1,7,5,6,9]
    
#     # Plot..
#     plt.plot(x_cor,y_cor)
    
#     #Add a title    
#     plt.title("Test Plot")
    
#     # Set the axis limits
#     plt.xlim(xmin = -3,xmax = 10)
#     plt.ylim(ymin = -3,ymax = 10)
    
#     # Add labels to the plot
#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")
    
#     # Add a grid
#     plt.grid(True)
    
#     # Display the line graph
#     plt.show()
    
# main()

"""
xticks
yticks

"""

def main():
    x_cor = [0,1,2,3,4]
    y_cor = [0,3,1,5,2]
    
    # Plot..
    plt.plot(x_cor,y_cor)
    
    #Add a title    
    plt.title("Test Plot")
    
       
    # Add labels to the plot
    plt.xlabel("Years")
    plt.ylabel("Sales")
    
    # Add tick marks
    plt.xticks([0,1,2,3,4],["2016","2017","2018","2019","2020"])
    plt.yticks([0,3,1,5,2],["$ 0m","$ 1m","$ 2m","$ 3m","$ 4m"])
                            
                            
    
    # Add a grid
    plt.grid(True)
    
    # Display the line graph
    plt.show()
    
main()