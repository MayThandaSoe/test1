# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:14:29 2020

@author: Mahendra
"""
"""
Exception is an error that occures while a program is 
running....causing the program to abruptly halt..
"""

# print("Hello")
# print("World")
# print("Welcome back")
# print(Python)
# print("Mingalar")
# print("Par")


# def main():
#     num1 = int(input("Enter a number"))
#     num2 = int(input("Enter another number"))
    
#     result = num1 / num2
#     print("Result",result)
    
# main()

# def main():
#     num1 = int(input("Enter a number"))
#     num2 = int(input("Enter another number"))
    
#     if num2!= 0:
#         result = num1 / num2
#         print("Result",result)
        
#     else:
#         print("Cannot divide by zero")
    
# main()



# def main():
#     hrs = int(input("Hours"))
#     pay_rate = float(input("Hourly rate"))
    
#     gross_pay = hrs * pay_rate
#     print("Gross Pay",gross_pay)
    
# main()



# def main():
#     try:
#         hrs = int(input("Hours"))
#         pay_rate = float(input("Hourly rate"))
#         gross_pay = hrs * pay_rate
#         print("Gross Pay",gross_pay)
    
#     except NameError:
#         print("ERRROR")
    
# main()




# def main():
#     file_name = input("Enter a filename")
#     try:
#         infile = open(file_name,'r')
#         contents = infile.read()
        
#         print(contents)
        
#         infile.close()
        
#     except FileNotFoundError:
#         print("Error")
        
# main()
"""
Handling Multiple Exceptions

"""    
# def main():
#     file_name = input("Enter a filename")
#     try:
#         infile = open(file_name,'r')
#         contents = infile.read()
        
#         print(contents)
        
#         infile.close()
        
#     except FileNotFoundError:
#         print("file not found")
#     except ValueError:
#         print("Value Error occured")
#     except:
#         print("Error")
        
# main()


# def main():
#     try:
     
#         age = int(input("Enter your age"))
        
#     except FileNotFoundError:
#         print("file not found")
#     except NameError:
#         print("Value Error occured")
#     except:
#         print("Error")
        
# main()

# def main():
#     try:
     
#         name = str(input("Enter your name"))
#         age = int(input("Enter your age"))
        
  
#     except:
#         print("Error")
        
# main()


"""
Displaying an Exception's Default Error Message
"""
# def main():
#     try:
     
#         age = int(input("Enter your age"))
        
#     except ValueError as apple:
#         print(apple)
#     #age = int(input("Enter your age : "))
        
# main()

"""
Specify Exception as a type

"""

# def main():
#     try:
     
#         age = int(input("Enter your age"))
        
#     except Exception as apple:
#         print(apple)
#     #age = int(input("Enter your age : "))
        
# main()


"""
The else Clause
"""
# def main():
#     total = 0
#     try:
#         # infile = open("test.txt",'r')
        
#         # for line in infile:
#         #     amount = float (line)
#         #     total += amount
            
#         # infile.close()
#         age = int(input("Enter your age"))
#     except Exception as err:
#         print(err)
        
#     else:
#         #print(format(total,',.3f'))
#         print("Else block")
        
#     finally:
#         print("Final steps....")
#         print("Good Bye....")
# main()
