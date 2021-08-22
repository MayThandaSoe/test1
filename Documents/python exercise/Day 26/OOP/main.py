# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:28:19 2020

@author: Mahendra

Homework .. Program 10.13 to 10.19
"""


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#           return f'My pet name is {self.name} and {self.age} years old Animal'

# Dog = Animal("Sweety" , 7)  # Object
# print(Dog)   # <__main__.Animal object at 0x000001C326F6F850>




# Inspecting an object in the program gives us the result 
# containing the object's id.

# __repr__ method

"""
str() is used for creating output for end user while
repr() is mainly used for debugging and development.

__repr__()  returns a printable representation of the object, 
__repr__() is more useful for developers while __str__() is for end users.

"""


# class Person:
#     def __init__(self,first_name,last_name,age,address):
#         self.first_name = first_name
#         self.last_name  = last_name
#         self.age        = age
#         self.address    = address
        
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} {self.age} {self.address}"
    
#     def __repr__(self):
#         return f"{self.first_name} {self.last_name} {self.age}...Hello"


# def main():
#     p1= Person("Aung ","Kyaw",54,"Botatung") # object
#     print(f"{p1}")  # invoke   p1.__str__()
    
#     # !r conversion flag ..for __repr__()
#     # !s conversion flag ..for __str__()
    
#     print(f"{p1!r}")  
    
# main()




# class num:
#     def __init__(self):
#         self.__my_data=2323454322344  # private data
#         #self.__my_string = "I am private data"
         
# # Mutator method...setter...modified
    
#     def set__my_attribute(self,value):
#         self.__my_data=value
#         return self.__my_data
               
# # Accessor Method...getter

#     def get__my_attribute(self):
#         return self.__my_data
    
       
# data = num()

# print(data.get__my_attribute())  # Read private data from class
# print(data.set__my_attribute(150))


# class num:
#     def __init__(self):
#         self.__my_data=2323454322344  # private data
#         #self.__my_string = "I am private data"
         
# # Mutator method...setter...modified
    
#     def my_attribute1(self,value):  # change private data
#         self.__my_data=value
#         return self.__my_data
               
# # Accessor Method...getter
  
#     def my_attribute2(self):     # Read data
#         return self.__my_data
    
       
# data = num()

# print(data.my_attribute2())  # Read private data from class

# data.my_attribute1(2838)

# print(data.my_attribute2())


"""

Private data in Python are not actually hidden like in other
OOP language (java,C++)...
"""


        
# class Person:
#     def __init__(self,name):
#         self.__name = name
    
#     def get_name(self):
#         return self.__name
    
#     def set_name(self,data):
#         self.__name = data
#         return self.__name


# person1 = Person("Aung Aung")
# print(person1.get_name())

# person1.set_name("Mya Mya")

# print(person1.get_name())


"""
Using @property decorator method
"""
# class num:
#       def __init__(self):
#           self.__my_data=2323454322344
        
#     # Accessor Method...getter  
#     # read-only property
#       @property  
      
#       def my_attribute2(self):
#           return self.__my_data
        
#   # Mutator method...setter...modified
#   # write property

#       #property_name.setter 
#       @my_attribute2.setter
      
#       def my_attribute2(self,value):
#           self.__my_data=value
#           return self.__my_data
               
# data = num()   

# # Accessor Method ..Read the private data inside the class
# print(data.my_attribute2)
# # print(data.my_attribute2)

# # setter
# data.my_attribute2 = 100
# print(data.my_attribute2)
# print(type(data.my_attribute2))


# isinstance(variable_name,type)
# a = 100.678
# print(isinstance(a,int))
# print(isinstance(a,str))
# print(isinstance(a,float))



class Service:
    def __init__(self,fee):
        self._fee = fee
    #getter
    @property
    def fee(self):
        return self._fee
    
    #setter
    @fee.setter
    def fee(self,updated_fee):
        if updated_fee > 5000 and isinstance(updated_fee,int):
            self._fee = updated_fee
        else:
            print("Please enter the valid service fee")
            
    
cleaning=Service(5000)
print(cleaning.fee)

cleaning.fee = 8000
print(cleaning.fee)

# Read it again
print(cleaning.fee)

print(property()) #<property object at 0x000001458F448B38>


