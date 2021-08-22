# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:48:45 2020

@author: Mahendra

Homework
Page 438 - Program 8.3,8.4
Page 446 - Program 8.6,8.7

"""

# name = "Mg Kyaw Aung"
# # for data in name:
# #     print(data)
# # data = name[5]
# # print(data)
# #print(name[2],name[4],name[6],name[7],name[8])
# #print(name[32]) #IndexError: string index out of range
# data = len(name)
# print(data)


"""
Counting alphabets
"""
# def main():
#     count = 0
    
#     string = str(input("Enter your string to make counting :"))
    
#     for data in string:
#         if data == 'S' or data == 's':
#             count+=1
            
#     print("The letter T appears",count,'times...')
    
# main()
# data = 'Test'
# data1 = ' Debug'
# data3 = data + data1
# print(data3)

# string[start : end]

# name = "Aung Myo Kyaw and Hla Hla Htay"
# first_time = name[0 : 5]
# print(first_time)

# second = name[8:]
# print(second)

# third = name[:9]
# print(third)


"""
string1 in string2
string1 not in string2
"""
#data = 'Aung Myo Kyaw and Hla Hla Htay'
# if 'Myo' in data:
#     print("The string 'Hla' was found")
# else:
#     print("The string 'Hla' was not found")

# if 'Mya' not in data:
#     print("True")
# else:
#     print("False")

"""
string_name.method
"""


# def main():
#     string = str(input("Enter a string : "))
    
#     if string.isalpha():
#         print("The string contains only alphabetic characters")
#     elif string.isdigit():
#         print("The string contains only digits")
#     elif string.isspace():
#         print("The string contains only white space")
#     elif string.islower():
#         print("The letters in the string are lowercase")
#     elif string.isupper():
#         print("The letters in the string are uppercase")
#     elif string.isalnum():
#         print("The string contains alphanumeric")

# main()

#data = 'ABCDEFGH'
# print(data.lower())
# data1 = 'abcdefgh'
# print(data1.upper())

# data = '   ABCDEFGH    ASf '
# print("With whitespace:",data)
# #print("Without whitespace:",data.strip())
# data1 = data.strip('A')
# print(data1)

# data = 'ABCDEFGH'
# print(data.strip('EFGH'))

# data = '  ABCDEFGH  TY  TY '
# print(data.lstrip()) # leading
# print(data.rstrip()) # trailing


#data = ' ABCDEFGH '
#print(data.lstrip(' ABC')) # leading
#print(data.rstrip('GH ')) # trailing
#print(data.strip('AH ')) # trailing
#print(data.lstrip(' AH'))


# name= str(input("Enter your name..."))
# status = name.startswith('Mg')
# print("Status : ",status)


# last_name = str(input("Enter your last name "))
# status = last_name.endswith("Smith")
# print("Status : ",status)


# string = 'Four score and seven years ago'

# pos = string.find('apple')
# if pos != -1:
#     print("The position of the 'score is '",pos)
# else:
#     print('your inputed string was not found')
#     print("Poistion : ",pos)


# string = 'Four score and seven years ago'
# new_data = string.replace('score','month')
# print(new_data)

# def main():
#     for count in range(1,7):
#         print('X' * count)
        
#     for count in range(6,0,-1):
#         print('Z' * count)
        
# main()


"""
String Splitting
Return as List
"""

# def main():
#     string = 'Kyaw_Kyaw Mya Mya Aung Aung Mg Mg Zaw Zaw'
    
#     words = string.split()
#     print(words)
#     print(type(words))
# main()

# def main():
#     date = '12/28/2020'
#     data = "12,233,343"
    
#     date_list = date.split('/')
#     data_list = data.split(',')
    
#     print(date_list)
#     print(type(date_list))
    
#     print("Data1 : ",data_list)
    
# main()