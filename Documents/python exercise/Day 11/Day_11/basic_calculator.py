# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:53:19 2020

@author: Mahendra
"""


def main():
    data = int(input("Enter data 1"))
    data2 = int(input("Enter data 2"))
    mode = input("Enter Operation mode")
    if mode == "+":
        print(add(data,data2))
        
    elif mode == "-":
        print(sub(data,data2))
        
    elif mode == "/":
        print(div(data,data2))
        
    elif mode == "*":
        print(mul(data,data2))
    else:
        print("No function")
    
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mul(x,y):
    return x*y
    
main()