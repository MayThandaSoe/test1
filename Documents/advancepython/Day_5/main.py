#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:25:52 2020

@author: mtdsoe
"""


import numpy as np

# scalar = np.array(123)
# print(scalar)
# print("scalar rank:",scalar.ndim)

# vector = np.array([1,2,3,4,5,6,7])
# print(vector)
# print("vector rank:",vector.ndim)

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)
# print("matrix rank:",matrix.ndim)

# x = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[10,11,12],[10,11,12]],[[10,11,12],[10,11,12],[10,11,12]]])
# print(x)
# print("Tensor rank:",x.ndim)


# data = np.arange(10,19).reshape((3,3))
# print(data)

# print(data[0,0])
# print(data[0,1])
# print(data[0,2])
# print(data[1,0])
# print(data[1,1])

# print(data[1,2])

# print(data[2,0])

# print(data[2,1])

# print(data[2,1])

# data = np.arange(16).reshape(2,2,4)
# print(data)

# print(data[0,0,0])
# print(data[0,0,1])


# print(data[0,1,0])
# print(data[1,0,0])
# print(data[1,1,0])
# print(data[1,0,1])

data = np.arange(1,16).reshape(3,5)
print(data)


print("second row",data[1,:])
print(" ")
print("first Row",data[0,:])
print("third row",data[2,:])
print(" ")

print(" ")
print("middle three column",data[[1,1:3])
print(" ")
print("row all column 0",data[:,0])
print(" ")
print(data[:,2:3])










