# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 19:31:45 2020

@author: Mahendra
"""

# Formatted Strings
# f-string is faster than str.format() and % formatting...



# data = "Aung Aung"
# #print("My name is ",data)
# print(f'My name is {data}')


# x = 150
# print(f'The value in x :  {x}')

# f=3.25

# print(f'This will print out : {f}')
# print(f'This will print out : {f:.5f}')

# # data = "Aung Aung"
# # print(f'My name is {data} ')

# name = "Kyaw Aung"
# print("My name is ",name )
# print(f'My name is {name} ')

# print(f'{200+343+343}')
# print(f'{200-3}')
# print(f'{200*343*343}')

# name = "Danny"
# age = 50

# print(f'Hello, I am {name}..My age is {age}')
# print(f'{122 + 344}')

# name1= "DANNY"
# print(f'{name1.lower()}...')
# name2 = 'kyaw kyaw'
# print(f"{name2.upper()}")

# name3 = 'KYAW KYAW'
# print(f'{name2.lower()}...')

# data = "Kyaw Kyaw"
# data1 = "Maung Maung"
# data2 = "Hla Hla"

# show_data = (f'hi {data}...'
#               f"I am {data1}..."
#               f"My name is {data2}...")

# print(type(show_data))
# print(show_data)


"""
Field Width

> ..... right aligned
< ..... left aligned
= ..... padding
^ ..... Centered aligned
"""



# table2 = [12,323,454]
# for number in table2:
#     print(f'{number:10}')

# print()
    
# table = ['Kyaw Kyaw' , 'Mg Mg' , 'Mya Mya']
# for name in table:
#     print(f'{name:>20}')
    
# print(f'number     Square     Cube')
# for data in range(1,11):
#     #print(f'{data:2d}         {data*data:3d}         {data*data*data:4d}')
#     print(f'{data:2d}\t\t\t{data*data:3d}\t\t\t{data*data*data:4d}')


# Minimum Field Width  ...
# 3...Number in a field of 3 spaces
# 5...Number in a field of 5 spaces
# 8...Number in a field of 8 spaces
# print(f'number\t\tSquare\t\tCube')
# for data in range(1,11):
#     data = float(data)
#     #print(f'{data:2d}         {data*data:3d}         {data*data*data:4d}')
#     print(f'{data:5.2f}\t\t\t{data*data:6.2f}\t\t\t{data*data*data:8.2f}')




apple = 0.50
bread = 1.50
cheese = 2.35

num_apple  = 4
num_bread  = 5
num_cheese = 6

total_apple = apple * num_apple
total_bread = bread * num_bread
total_cheese = cheese * num_cheese

strApple = "Apples"
strBread = "Bread"
strCheese = "Cheese"

total = total_apple + total_bread + total_cheese

print(f'{"My Grocery List " : ^30s}')
print(f'{"=" * 40}')
print(f'{strApple}\t{num_apple:10d}\t\t${total_apple:>5.2f}')
print(f'{strBread}\t{num_bread:10d}\t\t${total_bread:>5.2f}')
print(f'{strCheese}\t{num_cheese:10d}\t\t${total_cheese:>5.2f}')
print(f'{"Total" : >17s}\t\t ${total:>2.2f}')