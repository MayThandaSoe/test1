# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:57:29 2020

@author: Mahendra
"""

import numpy as np

# x = np.array([1,2,3])
# print(x)

# data = np.ones(3,dtype = np.int8)
# print(data)

# total = x + data
# print(total)

# a1 = np.array([10,20,30,40,50])
# a2 = np.arange(5)
# a3 = np.array([12,13,14,15,16])

# total = a1+a2+a3
# print(a1)
# print(a2)
# print(a3)
# print(total)

# a1 = np.array([100,200,300,400,500])
# a2 = np.array([10,20,30,40,50])
# print(a1)
# print(a2)
# results1 = a1-a2
# print(results1)

# print("-------------------------")
# print(a1)
# print(a2)
# results1 = a1*a2
# print(results1)
# print("-------------------------")

# print(a1)
# print(a2)
# results1 = a1/a2
# print(results1)


# A = np.array([[1,2,3],[4,5,6]])
# B = np.array([[7,8,9],[10,11,12]])
# C = A+B
# D = A*B # matrix multiplication

# print(C)
# print(D)

# Element-wise Operation
# A = np.arange(0,9).reshape(3,3)
# print("A")
# print(A)
# print("----------------------------")
# B = np.arange(10,19).reshape(3,3)
# print("B")
# print(B)
# print("----------------------------")

# print("C")
# C = A*B
# print(C)

# print("----------------------------")

# D = A@B # 
# print("D")
# print(D)

# print("----------------------------")

# E = B@A
# print("E")
# print(E)

# print("----------------------------")

# data = np.dot(A,B)
# print("Data")
# print(data)

# print("----------------------------")

# data1 = np.dot(B,A)
# print("Data 1")
# print(data1)

# data = np.array([1,2,3,4,5])
# data1 = data * 2
# print(data1)

# Brodcasting
# num1 = np.arange(1,6)
# print(num1)

# data1 = num1+2
# print(data1)
# print("----------------------------")


# num2 = np.linspace(1.1,5.5,5)
# print(num2)

# data2 = num2 + 3
# print(data2)
# print("----------------------------")

# num3 = num1 * num2
# print(num3)

"""
Comparing Arrays
"""

# num1 = np.arange(1,6)
# print(num1)
# num1 = np.arange(2,41,2).reshape(4,5)
# print(num1)
# #test1 = num1 >= 12
# #test1 = num1 == 12
# test1 = num1 < 30

# print("----------------------------")
# print(test1)

"""
Increment and Decrement Operator
"""
# a = np.arange(4)
# print(a)

# a+=5
# print(a)

# a-=2
# print(a)

# a*=4
# print(a)

"""
Create an array of the values from 1 through 5,then
use broadcasting to square each value.
"""
# data = np.identity(5)
# print(data)
# print("----------------------------")
# data1 = np.diag(np.arange(0,20,5))
# print(data1)


# data = np.arange(6).reshape(2,3)
# print(data)

# data1 = data.T
# print(data1)

# array1 = np.arange(15).reshape((3,5))
# print(array1)
# print("----------------------------")
# print(array1.T)

# array1 = np.arange(15).reshape((3,5))
# print(array1)
# print("----------------------------")
# array2 = np.random.randn(3,6)
# print(array2)

# temp = array1.T
# print(temp)

# res1 = np.dot(temp,array2)
# # res1= np.dot(array1,array2)
# print("----------------------------")
# print(res1)


# arr1 = np.arange(16).reshape(2,2,4)
# print(arr1)
# print("----------------------------")
# temp1 = arr1.T
# print(temp1)
# print("----------------------------")
# temp2 = arr1.swapaxes(0,2)
# print(temp2)
# print("----------------------------")
# temp2 = arr1.swapaxes(1,2)
# print(temp2)



x = np.array([[1,2,3],[5,6,7]])
print(x)

y =x.swapaxes(0,1)
print(y)
print("----------------------------")
z =x.swapaxes(1,0)
print(z)

a =x.swapaxes(0,2)
print(z)



# a = np.array([[23,45,67]])
# print(a)
# temp_a = a.swapaxes(0,1)
# print(temp_a)

# temp_b = a.swapaxes(0,2) # error
# print(temp_b)


# b = np.array([[[10,20],[23,45]],[[56,78],[89,90]]])
# print(b)
# print("----------------------------")
# temp_b = b.swapaxes(0,2)
# print(temp_b)
