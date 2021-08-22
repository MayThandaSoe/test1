# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:17:37 2020

@author: Mahendra
"""

import pickle

"""
Write
"""
# phone_book = {"Mg Aung" : '09347344',
#               "Kyaw Kyaw" : "09374733",
#               "Mg Hla" : "09475738"}

# # "wb" refers to binary writing....
# file = open("phonebook.dat",'wb')


# """
# dump function is used to serialize the object..
# """
# pickle.dump(phone_book,file)

# file.close()


"""
Read
"""
# 'rb' refers to read binary
# file = open('phonebook.dat','rb')

# """
# load function is used to retrive the data and unpickle
# """

# data = pickle.load(file)
# print(data)
# file.close()


# def main():
#     again = 'y'
    
#     o_file = open("data.dat",'wb')
    
#     while again.lower() == 'y':
#         save_data(o_file)
        
#         again = input("Enter more data ? (y/n)")
        
        
    
#     o_file.close()
    
# def save_data(file):
#     person = {}
    
#     person['name'] = input('Name : ')
#     person['Age']  = input("Age : ")
#     person['Weight'] = input('Weight : ')
#     person['Height'] = input("Height : ")
    
#     pickle.dump (person,file)

# main()
        
import this
# def main():
#     data = False
    
#     i_file = open("data.dat",'rb')
    
#     while not data:
#         try:
#             person_data = pickle.load(i_file)
#             display(person_data)
        
#         except EOFError:
#             data = True
            
#     i_file.close()
    
# def display(person):
#     print("Name : ", person['name'])
#     print("Age : " ,person['Age'])
#     print("Weight : ", person['Weight'])
#     print("Height : " ,person["Height"])
#     print()

# main()
