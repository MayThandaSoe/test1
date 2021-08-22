# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:34:25 2020

@author: Mahendra
"""

"""
Dictionary referred to KEY and VALUE pair
Known as Mapping

Dictionary_name = {Key : Value, Key : Value}
Data retrive...Dictionary_name [Key]


Homework 
Page 475 , Program 9.1
Page 477 , Program 9.2
"""



# phone_book = {"Aung Aung" : "0947377373",
#               "Kyaw Kyaw" : "0934574773",
#               "U Mya" : "08374732848343",
#               "U Hla" : "38432848343"}

# print(phone_book)
# print(phone_book["Aung Aung"])

# print(phone_book["U Mya"])

# print(phone_book["U Ma"])  KeyError
"""
Cannot have duplicate keys in Dictionary
"""
# Address_book = {'Kyaw Kyaw' : "Yangon",
#                 'Mya Mya'   : 'Bago',
#                 'Zaw Zaw'   : 'Pyay',
#                 'Aung Hla'  : 'Mandalay',
#                 'Hla Hla'  : 'Hpa an'}
#print(Address_book)
# print(Address_book['Aung Hla'])



# if 'Mg Hla' not in Address_book:
#     print(Address_book)






# print(data)
# print(data[123])
# print(data[12.23])
# print(data["Lat"])
# print(data["Long"])
# print(len(data))

"""
Deleting Elements
del dictionary_name[KEY]
"""

# del data[12.23]
# del data[123]
# print(data)

# temp = data["Long"]
# print(temp)
# print(type(temp))

# Empty Dictionary

# data1 = {}
#data1 = dict() #empty list
# data1["Zay Zay"] = 12342
# data1["Mya Mya"] = 3484.343
# data1["Zaw Aung"] = 304.342

# print(data1)

# for key in data:
#     print(key)

# for key in data:
#     print(key,data[key])

""""
Dictionary Methods


clear ----> dictionary_name.clear()
    . Clear the contents of Dictionary
    
get  ----> dictionary_name.get(key,default)
    . Get the value associated with Key..
    . If the key is not found,does not raise exception..
    . Instead it will return default value that speicfied
        in get method
        
items ----> Returns all the keys in dictionary as a sequence
            of Tuples (data1 = data.items())
            
keys -----> Returns all key in dictionary(data.keys())

values -----> Returns all value in dictionary(data.values())

pop ------> Returns the value associated with a key and 
            removes the key-value pair from the dictionary
            dictionary_name.pop(key,default)
            
popitem ---> Returns randomly selected key-value pair
            removes the key-value pair from the dictionary
            dictionary_name.popitem(key,default)
            
            
"""

# data = {'Kyaw Kyaw' : "Yangon",
#         'Mya Mya'   : 'Bago',
#          'Zaw Zaw'   : 'Pyay',
#          'Aung Hla'  : 'Mandalay',
#          'Hla Hla'  : 'Hpa an',
#          "Lat" : [10,20,30,40],
#          'Long' : (10.23,23.23,23),
#          "Mg Mg" : 2.433,
#          123 : 345,
#          12.23 : 234.343}

# print(data)
# data.clear()
# print("After using ",data)

# temp = data.get("Hla Hla","No Entry found")
# print(temp)

# temp1 = data.get("Aung Aung","No Entry found")
# print(temp1)


"""
Items() method, return style
([('Kyaw Kyaw', 'Yangon'), ('Mya Mya', 'Bago'), 
  ('Zaw Zaw', 'Pyay'), ('Aung Hla', 'Mandalay'), 
  ('Hla Hla', 'Hpa an'), ('Lat', [10, 20, 30, 40]), 
  ('Long', (10.23, 23.23, 23)), ('Mg Mg', 2.433), 
  (123, 345), (12.23, 234.343)])
"""


# for key,value in data.items():
#     print(key,value)
# data1 = data.items()
# print(data1)
# print(type(data1))

# temp = data.keys()
# print(type(temp))
# print(temp)
# for key in data.keys():
#     print(key)
# temp = data.pop('Zaw Zaw','Entry not found')
# print(temp)
# print(data)

# data1,data2 = data.popitem()
# print(data1,data2)
# k,v = data.popitem()
# print(k,v)
# k1,v1 = data.popitem()
# print(k1,v1)

# temp = data.values()
# print(type(temp))
# print(temp)
# for v in data.values():
#     print(v)