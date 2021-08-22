# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:47:34 2020

@author: Mahendra
"""

"""
Inheritance 
"""
# # Parent Class
# class Vehicle:
#     def __init__(self,color,model_num):
#         self.color = color
#         self.model_num = model_num
        
#     def description (self):
#         print(f"I am a {self.color} vehicle"
#               f" and my model is {self.model_num}..." )
        

# # Child class

# class Car(Vehicle):
#     def __init__(self,color,model_num,style):  # Child class initializer
#         super().__init__(color, model_num)  # Parent class initializer
#         self.style = style
        
#     def description(self):
#         print(f"I am a {self.color} car "
#               f"and my model is {self.model_num} "
#               f"and my style is {self.style}...")
        
        

# # Object
# print("From Parent class")
# v = Vehicle('Red','Toyota 99')
# v.description()
# print("##########################################")

# print("From Child class")
# c = Car("Black",'Toyota 99','SUV')
# c.description()



class Student(): # parent class
    def __init__(self,name,enroll_num):
        self.name = name
        self.enroll_num = enroll_num
        
    def show_data(self):
        print(f"I am {self.name} "
              f"my enroll number is {self.enroll_num} ...")

class College(Student): # child class 
    def __init__(self,name,enroll_num,admnyear,major):
        super().__init__(name,enroll_num)
        
        self.admnyear = admnyear
        self.major = major

    def show_data(self):
         
         print(f"I am {self.name}.. "
              f"my enroll number is {self.enroll_num} ..."
              f"my admission year is {self.admnyear} ..."
              f"my major is {self.major}...")
        


data = College("Kyaw Kyaw",345,2020,"Computer Engineering")
data.show_data()
print("##########################################")
print()

data1 = College("Mya Mya",375,2020,"Electronic Engineering")
data1.show_data()
print("##########################################")
print()

data2 = College("Aung Aung",545,2020,"Civil Engineering")
data2.show_data()
print("##########################################")
print()