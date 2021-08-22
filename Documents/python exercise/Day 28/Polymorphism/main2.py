# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:58:29 2020

@author: Mahendra
"""

# def my_print(a,b,c):
#     print(a,"is stored in a")
#     print(b,"is stored in b")
#     print(c,"is stored in c")
    
# my_print(1,2,3)


# def my_print(a,b,c=None):
#     print(a,"is stored in a")
#     print(b,"is stored in b")
#     print(c,"is stored in c")
    
# my_print(1,2)

# def my_print(a= None,b= None,c=None):
#     print(a,"is stored in a")
#     print(b,"is stored in b")
#     print(c,"is stored in c")
    
# my_print(c=3,a=5)

"""

The * is most commonly associated with mulitplication,
but in Python it doubles as the splat operator..
Unpacking

"""
# Unpacking
# a = [1,2,3,4]
# b = [*a,67,56,45]
# c = [*b,545,454]
# e = [12,212]
# d = [23,*e]
# print(a)
# print(b)
# print(c)
# print(d)

"""
*arg is short for arguments,and
**kwargs is short for keyword arguments

"""

# def my_sum(*args):
#     data = 0 
#     x = 0
#     for x in args:
#         data += x
#     return data

# # Function argument as a Tuple
# result = my_sum(100,1200,232,345,676,3456,3455434,245633)
# print(result)


# def print_scores(student,*score):
#     print(f"Student Name : {student} ..")
#     for data in score:
#         print(data)

# print_scores("Aug Aung",100,200,300,400,500,600,700,800 )



"""
"args" is a standard convention but still just a name
The secret revealed, in *args, the single asterisk is 
the real player

"""
# def test_var (f_arg,*argv):
#     print("First normal arg : ",f_arg)
#     for arg in argv:
#         print("Another arg through * argv : ",arg)
        
# test_var("Mg Mg","Python","Apple","Test")


"""
The double asterisk form of **kwargs us used to pass 
a keyworded variable-length argument dictionary to a function

Again,the two asterisks(**) are the important element here,
as the word kwargs is convenionally used,through not enforced
by the language

The name does not matter ,but the double asterisks create a
whose contents are keyword arguments - after those defined
from a function call..
"""
# def test_kwargs(**kwargs):
#     print(kwargs)
    
# test_kwargs(test1 = 'apple',test2 = 'orange',test3 = 'pineapple')



# def my_print(**kwargs):
#     for key,value in kwargs.items():
#         print("The value of {} is {}" .format(key,value))
        
# my_print(name = "Kyaw Kyaw",your_name = "Mya Mya")
        
def printPetNames(owner,**pets):
    print(f"Owner Name : {owner}")
    
    for pet,name in pets.items():
        print(f"{pet} : {name} ")
        
printPetNames("Zaw Zaw", Cat = "Pussi",Dog=['Aung Nak',"Jacky","Danny"],
              elephant = "Moe Moe")
