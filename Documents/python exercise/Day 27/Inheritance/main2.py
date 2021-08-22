# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:48:08 2020

@author: Mahendra
"""

"""
Multiple Inheritance
"""

class University: # parent class
    def __init__(self,admnyear,major):
        self.admnyear = admnyear
        self.major = major
        
    def show_data(self):
        
        print(f"my admission year is {self.admnyear} ..."
              f" my major is {self.major}...")
        
        
class College: # parent class
    def __init__(self,name,enroll_num):
        self.name = name
        self.enroll_num = enroll_num
        
    def show_data(self):
        print(f"I am {self.name} "
              f"my enroll number is {self.enroll_num} ...")


# Multiple Inherits
class Student(University,College): # child class 
    def __init__(self,name,enroll_num,admnyear,major,GPA):
        University.__init__(self, admnyear, major)
        College.__init__(self,name,enroll_num)
        
        self.GPA = GPA

    def show_data(self):
        print(f"I am {self.name}.. "
              f"my enroll number is {self.enroll_num} ..."
              f"my admission year is {self.admnyear} ..."
              f"my major is {self.major}..."
              f" my final year GPA is {self.GPA} ..")
         
         
data = Student("Kyaw kyaw",1232,2020,"Computer Engineering",4.7)
data.show_data()