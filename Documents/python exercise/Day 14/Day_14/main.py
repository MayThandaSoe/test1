# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:28:53 2020

@author: Mahendra
"""


# Reading file contents with for loop

# def main():
#     file = open("sales.txt",'r')
        
#     for line in file:
#         amount = float(line)
#         print(format(amount,'.2f'))
        
#     file.close()
    
# main()

"""
Processing the record
"""

# def main():
    
#     num_people = int(input("How many emmployee records" +
#                            "do you want to create?"))
    
#     file = open("employees.txt",'w')
    
#     for count in range(1,num_people +1):
#         print("Enter data from employee",count , sep ='')
        
#         name = input("Name : ")
#         id_num = input("ID Number : ")
#         dept = input("Department : ")
        
#         file.write(name + '\n')
#         file.write(id_num + '\n')
#         file.write(dept + '\n')
        
#         print()
        
#     file.close()
#     print("Records written to employees.txt file...")
# main()


"""
Reading a record from file
"""

# def main():
#     file = open('employees.txt','r')
#     name = file.readline()
    
#     while name != '':
#         id_num = file.readline()
#         dept = file.readline()
        
#         name = name.rstrip('\n')
#         id_num = id_num.rstrip('\n')
#         dept = dept.rstrip('\n')
        
#         print("Name : ",name)
#         print("ID Number : ",id_num)
#         print("Department : ",dept)
#         print("*****************************")
        
#         name = file.readline()
#     file.close()
# main()

"""
This program adds coffee inventory records to
the coffee.txt file
"""

# def main():
#     another = 'y'
#     coffee_file = open('coffee.txt','w')
    
#     while another == 'y' or another == 'Y':
#         print("Enter the following coffee data")
#         name = input ("Description : ")
#         qty = input ("Quantity (in pounds )")
        
#         coffee_file.write(name + '\n')
#         coffee_file.write(str(qty) + '\n')
        
#         print("Do you want to add another record")
        
#         another = str(input("Y = yes ,N = no"))
#     coffee_file.close()
#     print("Data written to coffee.txt file...")
# main()

"""
Reading Data from file....
"""

# def main():
#     file = open("coffee.txt",'r')
    
#     name =file.readline()
    
#     while name != '':
#         qty = float(file.readline())
        
#         name = name.rstrip('\n')
#         print ("Description : ",name)
#         print("Quantity : ",qty)
#         print("***********************************")
        
#         name = file.readline()
#     file.close()
    
# main()

"""
This program allows the user to search the coffee.txt file
for records matching a description
"""

def main():
    
    found = False # Boolean Flag
    
    search = str(input("Enter a name to search for  "))
    
    file = open("coffee.txt",'r')
    
    name = file.readline()
    print(name)
    
    while name != '':
        qty = file.readline()
        
        #qty = qty.rstrip('\n')
        name = name.rstrip('\n')
        qty = float(qty)
        
        if name == search :
            print("Description : ",name)
            print("Quantity : ",qty)
            print("Quantity Type",type(qty))
            print()
            found = True
        
        name = file.readline()
    file.close()
    
    if not found:
        print("That item was not found in the file...")
main()
        
        
"""
Homework 
Page - 331 (Program 6.11)
Page - 332 (Program 6.12)
Page - 341 (Program 6.18)
Page - 344 (Program 6.19)

"""

    