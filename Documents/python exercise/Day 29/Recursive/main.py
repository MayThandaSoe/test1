# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:51:55 2020

@author: Mahendra
"""

# def main():
#     message(5)
    
# def message(times): # message (5)
#     if times > 0:
#         print("THis is a recursive function")
#         message(times-1) # message (5-1)
  
# main()

# fact(5)...1 x 2 x 3 x 4 x 5
# fact(6)...1 x 2 x 3 x 4 x 5 x 6
# fact(7)...1 x 2 x 3 x 4 x 5 x 6 x 7



# def main():
#     number = int(input("Enter a non-negative number"))
    
#     fact = factorial(number)
#     print("The factoiral of ",number,'is',fact)
    
# def factorial(data):
#     if data == 0:
#         return 1
#     else:
#         return data * factorial(data - 1)
#             # 7 * (factorial(6))*
    
# main()

# def main():
#     numbers = [1,2,3,4,5,6,7,8,9,10]
#     my_sum = range_sum(numbers, 1,4)
#     print("The sum of items : ",my_sum)


# def range_sum (num_list,start,end):
#     if start > end:
#         return 0
#     else:
#         return num_list[start] + range_sum(num_list, start +1, end)
    

# main()


# def main():
#       print('The first 10 numbers in the')
#       print('Fibonacci series are:')

#       for number in range(1, 11):
#           print(fib(number))


# def fib(n):
#       if n == 0:
         
#           return 0
#       elif n == 1:
         
#           return 1
#       else:
#           return fib(n-1) + fib(n-2)
     
                 
        
#main()


def main():

      num1 = int(input('Enter an integer: '))
      num2 = int(input('Enter another integer: '))

      print('The greatest common divisor of')
      print('the two numbers is', gcd(num1, num2))

def gcd(x, y):
      if x % y == 0:
          return y
      else:
          return gcd(x, x % y)
     
        
main()