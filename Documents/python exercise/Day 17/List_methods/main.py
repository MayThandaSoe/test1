# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:34:42 2020

@author: Mahendra

Home work - Program 7.3 to 7.12 
"""

# data = [1,2,3,4,5,"Date",3843.242]
# print(data)

"""
Append Method...
Adds items to the end of the list
"""

#my_list = [] # empty list
# my_list.append(100)
# print(my_list)
# my_list.append("Hello")
# print(my_list)

#TypeError: append() takes exactly one argument (2 given)
#my_list.append("234.343",24332.343)
#(my_list)

"""
Extend Method...
..used to add more than one elements
can be used with Tuples,List and Set
"""

# color = ['orange','yellow','black','green']
# #color.append(['blue','white'])
# print(color)
# color.extend(['violet','white','blue'])
# color.extend(['Magenta'])
# print(color)



"""

Remove method...delete the elements with specified value
Clear method....delete all the elements in List
"""


# color = ['orange','yellow','black','green']
# print("Before remove",color)
# color.remove('black')
# print("After remove",color)

# color.clear()
# print(color)

"""
Index Method
"""
# data = ['orange',1.232,234,455.53,334,'Fruit',23,'Mango']
# index_number = data.index('Fruit') 

# print("Index Number : ",index_number)
# data[index_number] = 3.2343243    # data[5]= 3.2343243
# print(data)


"""
Insert Method....Insert list element with specific position
insert(index,items)
"""

# data = ['orange',1.232,234,455.53,334,'Fruit',23,'Mango']
# print(data)
# print(data[0])
# print(data[1])

# data.insert(1,"Pineapple")
# print(data)

# data.insert(4,"Pineapple")
# print(data)

# data.insert(6,"Tiger")
# print(data)

"""
Reverse Method
"""
# data = ['orange',1.232,234,455.53,334,'Fruit',23,'Mango']
# print(data)
# data.reverse()
# print(data)

"""
sorting method
"""

# my_data=[3,56,7,5,43,456,334,67,8,88,7,6543,12345,6677,43]
# print(my_data)
# my_data.sort()
# print(my_data)

"""
Count Method..used with single argument
"""
# data = ['orange','Fruit',1.232,234,'Fruit',455.53,334,'Fruit',23,'Mango']
# print(data)
# count_value = data.count('Mango')
# count_value1 = data.count('Fruit')
# print(count_value1)


"""
pop method
Remove the item at the given position in the list and return it..
if no index is specified.pop() removes and returns the last item
in the list
"""

# data = ['orange','Apple',1.232,234,'Durian',455.53,334,'Fruit',23,'Mango']
# print(data)

# # pop_data = data.pop() # no index..delete last item
# # print(pop_data)
# # print(data)

# my_index = data.index("Durian")
# print(my_index)

# pop_items = data.pop(my_index) # data.pop(4)
# print(pop_items)

# print(data)

"""
List Copying
"""

# # list1 = [1,2,3,4]
# # print(list1)
# # list2 = list1
# # print(list2)
# list1 = [1,2,3,4,5]
# list2 = list1.copy()
# print(list2)

"""
min,max
"""

# my_data=[3,56,7,5,43,456,334,67,8,88,7,6543,12345,6677,43]
# print("The highest value",max(my_data))
# print("The lowest value",min(my_data))


"""
del statment
"""
my_data=[3,56,7,5,43,456,334,67,8,88,7,6543,12345,6677,43]
print(my_data)
del my_data[1]
print(my_data)