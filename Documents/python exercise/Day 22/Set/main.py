# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:03:12 2020

@author: Mahendra

Homework...Page 508 - NO.4 and NO.6
"""

#my_set = set() # empty set

# myset= set(['a','b','c','d','e'])
# print(myset)
# print(type(myset))

# my_set = {'a',12,23.34,'apple','orange'}
# print(my_set)
# print(type(my_set))
# print(len(my_set))

# set expected at most 1 argument, got 3
# TypeError
# set1 = set('a','b','c')  # error
# set2={'a','b','c'}

# print(set2)

"""
Adding and Removing Elements
"""

# myset= set()
# myset.add(1)
# myset.add(2)
# myset.add(2)
# myset.add("Apple")
# myset.add("Orange")
# myset.add("Pineapple")
# print(myset)
# print("Type : ",type(myset))

# #myset.update([56.43,343.343,3453.3534])
# myset.update('abc')
# myset.update([12,23,56])
# print(myset)


# myset.remove(2)
# print(myset)

# myset.discard("Apple")
# print(myset)
# myset.discard("Orange")
# print(myset)

# # KeyError:
# myset.remove(38)

# # If we used discard(),it will not raise the exception..
# myset.discard(38)
# print(myset)

# # myset.clear()
# # print(myset)

"""
Using for loop
"""
# myset = set(['a','b','c','d','e'])
# for data in myset:
#     print(data)




"""
Using in or not in Operator
"""
# myset = set(['a','b','c','d','e'])
# # if 'b' in myset:
# #     print("Value is in the set...")
    
# # else:
# #     print("Error")

# if 233 not in myset:
#     print("Value is not in the set...")
    
# else:
#     print("Error")


"""
Union
set1 | set2
set1.union(set2)
"""

# set1 = set([1,2,3,4,5,6])
# set2 = set(["Apple","Orange","Mango","Durian"])

# #set3 = set1.union(set2)

# # using | operator to find the union of two set
# set3 = set1 | set2 
# print(set3) 


"""
Intersection 
set1 & set2
set1.intersection(set2)
"""

# set1 = set([1,2,3,4,5,6])
# set2 = set([3,4,6,8,9,56])

# #set3 = set1.intersection(set2)

# # using & operator to find the intersection of two set
# set3 = set1 & set2 
# print(set3) 


# """
# Difference
# set1-set2
# set1.difference(set2)
# """

# set1 = set([1,2,3,4])
# set2 = set([3,4,5,6])

# set3 = set1.difference(set2) # set1-set2
# set4 = set2.difference((set1)) # set2-set1

# data = set1 - set2
# data1 = set2 - set1

# print(set3) 
# print(set4)
# print(data)
# print(data1)


"""
Symmetric Difference
set1.symmetric_difference(set2)
set1 ^set2
"""

# set1 = set([1,2,3,4])
# set2 = set([3,4,5,6])
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set4 = set1 ^set2
# print(set4)


"""
Subset and Superset
"""

# set1 is a superset of set2
set1 = set([1,2,3,4]) # superset

# set2 is a subset of set1
set2 = set([2,3]) # subset

# print(set2.issubset(set1))
# print(set1.issuperset(set2))


# print(set1.issubset(set2))
# print(set2.issuperset(set1))


print(set2 <= set1)
print(set1 >= set2)

print(set1 <= set2)
print(set2 >= set1)