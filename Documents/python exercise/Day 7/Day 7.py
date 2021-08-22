#for data in [1,2,3,4,5,6,7,8]:
#    print(data)

#for data in "Mingalar Par":
#    print(data , end=" ")
    
    
#for num in [1,2,3,45,67,34.34]:
#    print(num)
    
#for name in ['Aung','Kyaw','Myo','Susan']:
#    print(name,end = ' ')

#color=['red','green','black','blue','yellow']
#for data in color:
#    print(data)

## range(stop)
#for data in range(8):
#    print(data)
#    
## range(start,stop)
##
#for data in range(3,9):
#    #print(data)
#    print("Welcome to Python for loop")
#    
#for data1 in range(-3,0):
#    print(data1)
#    
## range(start,stop,step)
#for data in range(2,12,3):
#    print(data)

# This program uses a loop to display a table
# showing the numbers 1 through 10 and their squares
#
#print('Number\tSquare')
#print("----------------")
#
#for number in range(1,11):
#    square = number ** 2
#    print(number,'\t',square)

# MPH = KPH * 0.6214
# KPH ... 60 ..130
# THis program converts the speed 60 kph through 130 kph...(in 10 kph increment)

#start_speed = 60
#end_speed = 130
#increment = 10
#conversion_factor = 0.6214
#
#print('KPH\tMPH')
#print('--------------')
#
#for kph in range(start_speed,end_speed,increment):
#    mph = kph * conversion_factor
#    print(kph,'\t',format(mph,',.2f'))
#
#

#start = int(input("Enter the starting number"))
#end = int(input("Enter ending limit"))
#print('Number\tSquare')
#print("----------------")
#
#for number in range(start,end):
#    square = number ** 2
#    print(number,'\t',square)

# Running Total

#max_value = 8
#
## Initialize an accumulator variable
#total =0
#
#print("This program calculates the sum of ")
#print(max_value,' number you will enter...')
#
## get then number and accumulate them
#for count in range(max_value):
#    number = int(input("Enter a number : "))
#    total = total + number
#    #total = total + 5 # total = total + 1
#
#print("The total is ",total)
#
#
#hours = int(input("Enter the hours worked"))
#pay_rate = float(input("Enterthe hourly pay rate"))
#
#gross_pay = hours * pay_rate
#print(gross_pay)  # computer error

# retail price = wholesale x 2.5
# without validation

#mark_up = 2.5
#another = 'y'
#
#while another == 'y' or another == 'Y':
#    wholesale = float(input("Enter the item's wholsale cost"))
#    
#    retail = wholesale * mark_up
#    print("Retail price : $",format(retail,',.2f'),sep=" ")
#    
#    another = str(input("Do you want to add another item"))
    
# with validation

mark_up = 2.5
another = 'y'

while another == 'y' or another == 'Y':
    wholesale = float(input("Enter the item's wholsale cost"))
    
    # Input Validation ..Validate the wholsale cost...
    while wholesale <= 0 :
        print("ERROR : the cost cannot be negative value and zero")
        wholesale = float(input("Enter the item's wholsale cost"))
        
    
    retail = wholesale * mark_up
    print("Retail price : $",format(retail,',.2f'),sep=" ")
    
    another = str(input("Do you want to add another item"))