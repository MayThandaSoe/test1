# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:48:16 2020

@author: Mahendra
"""

# Polymorphism

# Creating a shape Class 
# class Shape: 
#     width = 0 
#     height = 0 
  
#     # Creating area method 
#     def area(self): 
#         print("Parent class Area ... ") 
  
  
# # Creating a Rectangle Class 
# class Rectangle(Shape): 
  
#     def __init__(self, w, h): 
#         self.width = w 
#         self.height = h 
  
#     # Overridding area method 
#     def area(self): 
#         print("Area of the Rectangle is : ", self.width*self.height) 
  
  
# # Creating a Triangle Class 
# class Triangle(Shape): 
  
#     def __init__(self, w, h): 
#         self.width = w 
#         self.height = h 
  
#     # Overridding area method 
#     def area(self): 
#         print("Area of the Triangle is : ", (self.width*self.height)/2) 
  
  
# rectangle = Rectangle(10, 20) 
# triangle = Triangle(2, 10) 
  
# rectangle.area() 
# triangle.area() 



# test = isinstance(100,int)
# print(test)
# test1 = isinstance(12.343,int)
# print(test1)
# test2 = isinstance(12.343,float)
# print(test2)





class A:
    def forward(self):
        print("I am going forward...I am from class A")
        

class B(A):
    def forward(self):
        print("I am also going forward but I am from class B")
        

a_obj = A()
b_obj = B()

a_obj.forward()
b_obj.forward()






