# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:20:41 2020

@author: Mahendra
"""



"""
Creating class
"""
class Animal:
    
    # data attribute
    data1 = 100
    data2 = 200
    data3 = 2.232
    data4 = "I am from Animal class"
    
    # methods
    def fun1(apple):
        apple.name = "I am Jacky"
        print("Name : ",apple.name)
        
        apple.age = 10
        print("Age : ",apple.age)
        
        
    def fun2(self):
        self.name = "I am Sweety"
        print("Name : ",self.name)
        
        self.age = 12
        print("Age : ",self.age)
        
    

"""
Creating instance of class (Object)
"""

Dog = Animal()   # Obj1
Cat = Animal()   # Obj2
elephant = Animal()

print(Dog.data1)
print(Dog.data2)
print(Dog.data3)
print(Dog.data4)

print(Cat.data1)
print(Cat.data2)
print(Cat.data3)
print(Cat.data4)

Dog.fun1()
Dog.fun2()

Cat.fun1()
Cat.fun2()

print(type(Dog))
print(type(Cat))


# x= 100
# y=12.34
# z="I am a string"

# print(z.upper())

# print("Type of x : ",type(x))
# print("Type of y : ",type(y))
# print("Type of z : ",type(z))

# my_list = [1,2,3,4,5]
# my_list.append("apple")

# print("Type of my_list : ",type(my_list))
