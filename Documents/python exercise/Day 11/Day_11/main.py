# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:09:34 2020

@author: Mahendra
"""


# def main():
#     data = add(20,10)
#     data1 = data+ 100
#     print(data1)
#     sub(30,20)
    
#     #next_data = sub(30,20)
#     #print(next_data)
#     #test = next_data + 150
#    # print(test)
    
    
# # Value returning Fuction
# def add(x,y):
#     return x+y # return

# # void function
# def sub(x,y):
#     result = x-y
#     print(result)  # display output
    
    
# main()


# Write a calculator with addition,
# diviion,subtraction and multiplication..
# Ask data and function from user


# import math
# from datetime import date

# today = date.today()
# print(today)

# def main():
#     num = float(input("Enter a number"))
    
#     square_root = math.sqrt(num)
#     print("The square root of ",num, 'is ' , square_root)
    
# main()

# import random as task


# def main():
#     for count in range(8):
#         number = task.randint(1,100)
#         print("The number is",number)
#         print(number+1)
    
# main()


import random as ra

min = 1
max = 6

def main():
    again = 'y'
    
    while again == 'y' or again == 'Y':
        print("Rolling the dice...")
        print("Their values are...")
        print(ra.randint(min,max))
        
        again = str(input("Do you want to roll them again ? (y = yes)"))
        
main()






