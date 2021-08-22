# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:39:19 2020

@author: Mahendra
"""

import numpy as np


# my_list = [1,2,3,4,5]
# print(my_list)
# print(type(my_list))

# arr1 = np.array(my_list)
# print(arr1)

# print(type(arr1))

# data = np.array([10,20,30,40,50])
# print(data)
# print(type(data))

# print(data.max())

# data1 = np.array([6.5,34.45,4,5,6,78])
# print(data1)

# print(type(data1))

"""

1 Byte = 8bit
int8,uint8.... 1 Byte
int16,uint16...2 Byte
int32,unit32.. 4 Byte
int64,unint64..8 Byte

"""
# data = np.array([[1,2,3,4,5],
#                 [6,7,8,9,10]])

# # print(data)
# # print(type(data))

# # print(data.ndim)
# # print(data.shape)
# print(data.size)
# print(data.dtype)    # data type
# print(data.nbytes)   # Total number of byte...Array


# data1 = np.array([[1,2],
#                   [3,4],
#                   [5,6]])

# print(type(data1))
# print(data1.ndim)
# print(data1.shape)
# print(data1.size)
# print(data1.dtype)
# print(data1.nbytes)


# data = np.array([1.2,3.4,5.6,7.8,9.2])
# print(data.dtype)
# print(data.size)
# print(data.nbytes)

# data = np.array([1,2,3,4],dtype = np.int64)
# print(data)
# print(data.dtype)

# data1 = np.array([1,2,3,4] ,dtype = np.float)
# print(data1)
# print(data1.dtype)

# data3 = np.array([1,2,3,4,5] , dtype = np.complex)
# print(data3)
# print(data3.dtype)


# data = np.array([1,2,3,4,5] , dtype = complex)
# print(data)
# print(data.real)
# print(data.imag)
"""
Once a Numpy array is created, its dtype cannot be changed,other than
by creating a new copy with type-casted array values.

Typycasting an array is straightforward and can be done using either
np.array function

"""
# data1 = np.array([1.34333,4.52442,6.742,8.93] ,dtype = np.int8)
# print(data1)
# print(data1.dtype)

# data1 = np.array(data1,dtype = np.float32)
# print(data1)
# print(data1.dtype)

# data1 = np.array([1,2,3,4,5] , dtype = np.float)
# print("Data1 : ",data1)
# data2 = np.array([5,6,8,3,9] , dtype = np.complex)
# print("Data2 : ",data2)

# data3 = data1 + data2
# print("Data3 : ",data3)
# my_str = np.array(['Test1','Test2','Test3'],dtype = np.string_)
# print(my_str)


"""
If you have an array of strings representing numbers, you can use
astype to convert to numeric form...
"""
# my_str = np.array(['1.2','3.4','5.6','7.8'],dtype = np.string_)
# print(my_str)
# print(my_str.dtype)
# data= my_str.astype(np.float)
# print(data)
# print(data.dtype)

# data1 = np.array([3.6,3.4,6.7,8.9,9.8])
# print(data1)

# data2 = data1.astype(np.int32)
# print(data2)