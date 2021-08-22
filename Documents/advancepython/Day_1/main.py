#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:39:37 2020

@author: mtdsoe
"""


import numpy as np

# my_list = [1,2,3,4,5]

# print(my_list)
# print(type(my_list))

# arr1 = np.array(my_list)

# print(arr1)

# print(type(arr1))

# arr1 = np.array([1,2,3,4])
# print(arr1)

# print(type(arr1))

# print(np.max())

data = np.array([[1,2,3,4,5]
                 ,[6,7,8,9,10]])

print(type(data))

print(data.ndim)

print(data.shape)
print(data.size)
print(data.dtype)
print(data.nbytes)

data = np.array([1,2,3,4],dtype=np.complex)
print(data)
print(data.dtype)
print(data.real)
print(data.imag)

data = np.array([1.3,4.5,6.7,8.9],dtype=np.float128)
print(data)
# print(data.dtype)
# print(data.real)
# print(data.imag)

# data1 = np.array([1.3,4.5,6.7,8.9],dtype=np.float128)
# print(data1)

# data = np.array([1,2,3,4],dtype=np.complex)
# print(data)

# data2= data1 + data
# print(data2)


# my_str = np.array(['Test1','Test2','Test3'],dtype=np.string_)
# print(my_str)

my_str = np.array(['1.2','3.4','5.6'],dtype=np.string_)
print(my_str)

data=my_str.astype(np.float)
print(data)
print(data.dtype)