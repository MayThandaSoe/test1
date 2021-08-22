# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:09:57 2020

@author: Mahendra
"""

"""
2-D List

List_name [ROW][COL]
"""

# data = [["Mg Mg","Mya Mya",'Aung Nak'],
#         ['Kyaw Kyaw','Hla Hla',23.2433],
#         ['Su Su','Aye Aye',43]]
# print(data[0][2])
# print(data[1][2])
# print(data[2][2])

# scores = [[90,93,100],
#           [67,87,98],
#           [87,98,69]]   

# print(scores[2][1])
# print(scores[0][1])
# print(scores[1][2])
# print(scores[2][2])

"""
Assign random numbers to 2D list
"""
# import random
# row = 3
# col = 4


# data = [[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]

# # Nested Loop
# for r in range(row):
#     for c in range(col):
#         data[r][c] = random.randint(1,100)
# print(data)


"""
Tuples
1. cannot be changed...Immmutable
2. Only Read access
3. parentheses ()
"""

# my_tuples = (1.23,454,343.343,"Apple","Mya Mya","e34",45.343,
#              "Dog","Cat" )

#print(len(my_tuples))
# for data in my_tuples:
#     print(data)
# for data in range(len(my_tuples)):
#     print(my_tuples[data])
#print(my_tuples(4)) # can only be used in function

# print(my_tuples[3])
# print(my_tuples[6])
# print(my_tuples[8])

#'tuple' object does not support item assignment
#my_tuples [5] = "Aung Aung"

# data = (1,)  # one element tuples
# print(data)
# print("Type : ",type(data))


# data1 = (1) # an integer
# print(data1)
# print("Type : ",type(data1))

"""
Converting Between Lists and Tuples

"""

data = (1,2,3,4,5,6,7,8)
print("Type : ",type(data))

# Python Built-in Function list()
# Covert to list
temp = list(data)
print("Inside Temp :",temp)
print("Type : ",type(temp))

temp[2] = 13
temp[4] = 15
temp[7] = 18
print("Updated Temp :",temp)


# Python Built-in Function tuple()
# Covert to Tuple
data = tuple(temp)
print("Inside Temp :",data)
print("Type : ",type(data))