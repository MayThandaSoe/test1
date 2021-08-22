# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 19:08:32 2020

@author: Mahendra
"""

# data = [10,20,30,45,4533,345]
# print(data)
# print("Type : ",type(data))

"""
Accessing Index...
list_name[index]
"""
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])
# print(data[5])  


# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw"]

# print(my_data)

# print(my_data[0])
# print(my_data[1])
# print(my_data[2])
# print(my_data[3])
# print(my_data[4])
# print(my_data[5])
# print(my_data[6])
# print(my_data[7])

# name = ["Mya Mya","Zaw Zaw","Aung Aung","Kyaw Kyaw","Aye Aye"]
# print(name)

"""
Repetition Operator

"""

# num = [0] * 5
# print(num)

# num1 = [1,2,3,4] * 3
# print(num1)

"""
len Function
"""
# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw",233,453]
# # data = len(my_data)
# # print(data)
# print(len(my_data))

"""
Accessing List elements with for loop

"""
# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw",233,453]

# for data in my_data:
#     print(data)


"""
Accessing List elements with while loop

""" 
# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw",233,453]

# index = 0

# while index < len(my_data):
#     print(my_data[index])
#     index+=1
    

# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw",233,453]

# print(my_data[-1])
# print(my_data[-2])
# print(my_data[-3])
# print(my_data[-4])
# print(my_data[-5])
# print(my_data[-6])
# print(my_data[-7])
# print(my_data[-8])
# print(my_data[-9])
# print(my_data[-10])
#print(my_data[-12])     IndexError
# print(my_data[13])     IndexError
    

"""
List are Mutable
list_name[index] = new value
"""
# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw",233,453]
# print(my_data)

# my_data[2] = "Mya Mya"
# my_data[4] = "Aung Aung"

# my_data[0] = 1.232
# my_data[5] = 34.343
# my_data[6] = 54.345
# my_data[8] = 78.565
# my_data[9] = 95.67


#print(my_data)


"""
Concatenating List
"""

# list1 = [1,2,3]
# print(list1)
# list2 = ["Apple","Orange","Pinapple"]
# print(list2)
# list3 = list1 + list2
# print(list3)



"""
Sales_list.py
"""

# days = 5

# def main():
#     sales = [0] * days
#     index = 0
    
#     print("Enter the sales for each day...")
    
#     while index < days:
#         print("Day #" , index + 1 , ":",sep ='',end='')
#         sales[index] = float(input())
#         index +=1
        
#     print("Here are the values you entered...")
        
#     for value in sales:
#         print(value)
# main()


"""
List Slicing
list_name [start : end]......[start : end-1]
"""

# my_data = [1,"apple",2.34,"orange",5.43,12,34,"Zaw Zaw",233,453]

# data1 = my_data[1 : 4]
# print(data1)


# data2 = my_data[4: ]
# print(data2)

# data3 = my_data[ :6]
# print(data3)

# data4 = my_data[0:6]
# print(data4)


# print(my_data[3:8])
# print(my_data[6:9])


"""
Finding items in List using in Operator
Usage.....item in list_name
"""


def main():
    product_name = ["A011","B012","C013","D014","D015"]
    
    search = str(input("Enter your product number : "))
    
    if search in product_name:
        print(search , "was found in the list")
    else:
        print(search,"was not found in the list...")
        
main()


