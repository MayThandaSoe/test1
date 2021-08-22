# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:38:30 2020

@author: Mahendra
"""
import matplotlib.pyplot as plt

# def main():
#     x_cor = [0,1,2,3,4]
#     y_cor = [0,3,1,5,2]
    
#     # Plot..
#     plt.plot(x_cor,y_cor,marker=">")
    
#     #Add a title    
#     plt.title("Test Plot")
    
       
#     # Add labels to the plot
#     plt.xlabel("Years")
#     plt.ylabel("Sales")
    
#     # Add tick marks
#     plt.xticks([0,1,2,3,4],["2016","2017","2018","2019","2020"])
#     plt.yticks([0,3,1,5,2],["$ 0m","$ 1m","$ 2m","$ 3m","$ 4m"])
                            
                            
    
#     # Add a grid
#     plt.grid(True)
    
#     # Display the line graph
#     plt.show()
    
# main()


"""
Bar Chart
"""


# def main():
#     l_edges = [20,40,60,80,100] # x- coordinates
    
#     # y- coordinates
#     height = [200,400,600,800,1000]
    
#     bar_width = 6
#     plt.bar(l_edges,height,bar_width,color = ('c','r','b','m','k'))
    
#     plt.show()
    
# main()


# def main():
#     l_edges = [20,40,60,80,100] # x- coordinates
    
#     # y- coordinates
#     height = [200,400,600,800,1000]
    
#     bar_width =9
#     plt.bar(l_edges,height,bar_width,color = ('c','r','b','m','k'))
    
    
    
#     #Add a title    
#     plt.title("Sales by Year")
    
       
   
#     plt.xlabel("Years")
#     plt.ylabel("Sales")
    
#     # Add tick marks
#     plt.xticks([20,40,60,80,100],["2016","2017","2018","2019","2020"])
#     plt.yticks([200,400,600,800,1000],["$ 0m","$ 1m","$ 2m","$ 3m","$ 4m"])
                            
                            
       
#     # Display the line graph
#     plt.show()
    
# main()

"""
Pie Chart
"""
# def main():
#     data = [20,40,60,80,100]
#     plt.pie(data)
#     plt.show()
# main()

def main():
    data = [100,200,300,400,500]
    lab = ['1st','2nd','3rd','4th','5th']
    
    plt.pie(data,labels = lab,colors = ('c','r','b','m','g'))
    
    plt.title("Simple Pie Chart")
    
    plt.show()
    
main()
    