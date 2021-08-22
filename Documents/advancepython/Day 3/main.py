# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:59:07 2020

@author: Mahendra
"""

import numpy as np
import matplotlib.pyplot as plt

# data = np.array([1,2,3,4,5])
# print(data)

# print(data.ndim)
# print(data.shape)

"""
Creates a full array of zeros with dimensions defined by 
the shape argument
dtype....float64
"""
# data1 = np.zeros((3,3))
# print(data1)
# print(data1.dtype)
# print(data1.ndim)
# print(data1.shape)

# data2 = np.ones((3,3))

# print(data2)
# print(data2.dtype)
# print(data2.ndim)
# print(data2.shape)
# data3 = np.zeros(4)
# data4 = np.ones(4)
# print(data3)
# print(data4)

# data = np.ones(5)
# print(data)
# print(data.dtype)

# data = np.ones(5, dtype = np.int64)
# print(data)
# print(data.dtype)

"""
Arrange() function generates Numpy arrays with numerical sequence
that respond to particular rules depending on the passed arguments.
If the third argument of the arrange() function is specified,
this will represent the gap between one value and next one.
np.arange(start,stop,step)
"""
# x = np.arange(0,10)
# print(x)
# print(x.ndim)
# print(x.dtype)

# y = np.arange(0,10,2)
# print(y)
# print(y.ndim)
# print(y.dtype)

# x_float = np.arange(0,5,0.6)
# print(x_float)
# print(x_float.ndim)
# print(x_float.dtype)

"""
reshape() functions is used to create a new shape to an array
without changing a data..
numpy.reshape(x,newshape)
"""

data = np.array([[1,2,3],[5,6,7]])
print(data)

data1 = np.reshape(data,(3,2))
print(data1)

"""
Return the tanspose of a matrix
If the matrix shape is (X,Y) , the transpose matrix shape will be
(Y,X)
"""
# data2= data.transpose()
# data3 = np.transpose(data)
# print(data3)
# print(data2)

# a = np.arange(0,12)
# print(a)
# b=a.reshape(3,4)
# print(b)

# c = np.arange(1,20,2).reshape(2,5)
# print(c)

# data = np.random.random(10)
# print(data)
# print(data.dtype)

# data1 = np.random.randint(3,10)
# print(data1)
# #print(data1.dtype)   Numpy array
# print(type(data1))
# test = np.ones((4,4)) * 15
# print(test)
# print(test.ndim)
# print(test.dtype)


"""
numpy.full(shape,fill,dtype)

shape ...number of rows
fill ... value to fill
"""
# test1 = np.full([4,4] , 15 ,dtype = np.int32)
# print(test1)

"""
empty() is used to create a new array given shape and type,
without initializing any entries..
empty(),unlike zeros() does not set the array values to zero,
and may therefore marginally faster...

"""
# data = np.empty(5)
# print(data)

# data1 = np.empty([3,3],dtype =  np.int8)
# print(data1)

# data = np.empty(4)
# data.fill(3)
# print(data)

"""
linespace.....Linear sequence generator

np.linspace(start,end,num,endpoint = False , retstep = False)

-- Generate a uniform sequence
-- num .. total number of point in a sequence
"""

# x = np.linspace(0,5,10)
# print(x)

# x = np.linspace(0.01,1,10,endpoint = False)
# print(x)
# print("Length : ",len(x))

# print("________________________________________")


# x = np.linspace(0.01,1,10,endpoint = True)
# print(x)
# print("Length : ",len(x))
# print("________________________________________")

# x = np.linspace(0.01,1,10,endpoint = True, retstep= True)
# print(x)
# print("Length : ",len(x))
 
# # v0 = 5
# # g = 9.81

# # t = np.linspace(0,1,1001,retstep = True)

# # y = (v0 * t) - (0.5*g*t**2)

# # plt.plot(t,y)
# # plt.xlabel("T (s)")
# # plt.ylabel("Y (m)")
# # plt.show()

# t = np.linspace(0,1,1001,retstep = True)
# print(t)