# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:18:35 2020

@author: Mahendra

Homework..
Program 10.5,10.6,10.7,10.8,10.9,10.10,10.12 and 10.13
"""

a = 100
a = 1.23
a = "String"


class Animal:
    
    # Initializer Method...known as constructor
    def __init__(self,name,age): # dunder function
        self.name = name
        self.age = age
        
    def eat(self):
        print("My name is ",self.name)
        print("I am eating now...")
    
    def sleep(self):
        print("My name is ",self.name)
        print("I am sleeping")
        

# Creating object to access inisde Animal class
dog = Animal("Aung Nat", 2)
cat = Animal ("My_cat",3)

dog.eat()
dog.sleep()

cat.eat()
cat.sleep()



class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        
    def say_hello(self):
        print("My name is ",self.name)
        print("I am ",self.age,"years old..")
        print("I live in....",self.address)
        
        
  
        



