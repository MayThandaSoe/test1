# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:15:54 2020

@author: Mahendra
"""


# def main():
#     value = 5
#     show_double(value)
    
    

# def show_double(num):
#     result = num * 2
#     print(result)

# main()

# def main():
#     addition(10,20)

# def addition (num1,num2):
#     print(num1 + num2)

# main()

# This program converts kilometer to miles

# def main():
#     kilometer = float(input("Enter kilometer : "))    
#     kilo_to_miles(kilometer)
    
    
# def kilo_to_miles(data):
#     result = data * 0.621371
#     print("Miles : ", result)

# main()

# This program demonstrates passing two string arguments to
# a function

# def main():
#     first_name = str(input("Enter your first name"))
#     last_name = str(input("Enter your last name"))
    
#     print("Your name is ")
#     print_name(first_name , last_name)
    
#     print("Your name reversed is ")
#     reverse_name(first_name,last_name)
    

# def print_name(first,last):
#     print(first , last)
    
# def reverse_name(first,last):
#     print(last,first)


# main()

# Making changes to Parameters
# This program demonstrates what happens when you changes
# the value of a parameter


# def main():
#     value = 100  # local variable
#     print("The value from main function is ",value)
#     change_me(value)  # change_me(100)
#     print("Back in the main..the value is still..",value)
    
    
    
# def change_me(data):  # data = 100
#     print("I am changing the value..")
#     data = 0
#     print("Now the value is",data)


# main()

# Keywords arguments

# def main():
#     #show_interest(10000,0.02,10)  # positional arguments
#     show_interest(rate = 0.02,priniciple = 300000,periods = 20)
    
#     # Not possible to mix postional arguments and keywords arguments
#     #show_interest(rate = 0.02,priniciple = 300000, 20) Error



# def show_interest(priniciple , rate , periods):
#     interest = priniciple * rate * periods
#     print("The simple interest  will be $ ",format(interest,',.2f'),sep='')

# main()




# def main():
#     first_name = str(input("Enter your first name"))
#     last_name = str(input("Enter your last name"))
    
#     print("Your name is ")
#     print_name(last = last_name ,first =first_name)
    
#     print("Your name reversed is ")
#     reverse_name(last = last_name ,first =first_name)
    

# def print_name(first,last):
#     print(first , last)
    
# def reverse_name(first,last):
#     print(last,first)
# main()


# Global Variable

# value = 123   # global variable

# def show_value():
#     print("Value :" , value)
    
# show_value()


# value = 0 # global variable

# def main():
#     global value
#     print("Original Global value :",value)
#     value = int(input("Enter a number"))
#     show_value()
    
# def show_value():
#     print("The number you entered is ", value)
    
# main()


# Program 5.15  (retirement.py)

CONTRIBUTION_RATE = 0.05  # global constant


def main():
    gross_pay = int(input("Enter the gross pay"))
    bonus = float(input("Enter the bonus amount"))
    show_pay(gross = gross_pay)
    show_bonus(bonus)
    
    
def show_pay(gross):
   #  global CONTRIBUTION_RATE
    # CONTRIBUTION_RATE = 10
    print(CONTRIBUTION_RATE)
    contrib = gross * CONTRIBUTION_RATE
    print("Contribution rate for gross pay : ",contrib)
    
def show_bonus(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print("Contribution rate for bonus : ",contrib)
    


main()










