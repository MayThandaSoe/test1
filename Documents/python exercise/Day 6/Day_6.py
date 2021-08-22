# Boolean Varaiable
# True = 1
# False = 0

#x= True
#y= False 
#
#data = int(input("Enter integer value"))
#
#if data >= 1000:
#    result = True
#    print(result)
#    if result :  # Use as a Flag
#        print("Your data value is more than thousand")
#else:
#    result = False
#    print(result)

#data= int(input("Enter your data"))
# assign as zero
#result = False
#result1 = False
#result2 = False
#if data > 1000 and data < 10000:
#    result = True
#elif data > 10000 and data < 20000:
#    result1= True
#elif data > 20000 and data < 30000:
#    result2 = True
#else:
#    result=False
#    result1=False
#    result2=False
# 
# Use as Boolean Flag
#if result:
#    print("Your data is between 1000 and 10000")
#elif result1:
#    print("Your data is between 10000 and 20000")
#elif result2:
#    print("Your data is between 20000 and 30000")
#else:
#    print("Error")

# Comparing String

#name1 = 'Mary'
#name2 = 'Mark'
#
#if name1 > name2:
#    print("Mary is greater than Mark")
#else:
#    print("Mary is not greater than Mark")

#name1 = str(input("Enter a name(last name first :)"))
#name2 = str(input("Enter another name(last name first : )"))
#
#print("Here are the names,listed alphabetically")
#
#if name1 < name2:
#    print(name1)
#    print(name2)
#else:
#    print(name2)
#    print(name1)

#if name1 == name2:
#    print("The names are the same")
#else:
#    print("The names are not the same")


#password = str(input("Enter the password"))
#
#if password == "Apple@12334":
#    print("Password Accepted....")
#else:
#    print("Sorry , that is wrong password....")



#data = 5
#sum = 0
#i = 1
#
#while i <= data :
#    sum = sum + i
#    i = i+1
#print("The sum result is " , sum)

#count= 0
#while count < 2:
#    print("Inside loop")
#    count = count+1
#else:
#    print("Outside loop")


#keep_going = 'y'
#
#while keep_going == 'y':                                # the condition is tested.
#    sales = float(input("Enter the amount of sales"))
#    comm_rate = float(input("Enter the commission rate"))
#    
#    commission = sales * comm_rate
#    
#    print("The commission is $ ",format(commission ,',.2f'),sep='')
#    
#    keep_going = str(input("Do you want to calculate another " +
#                               "Commission (Enter y for yes)"))
#    # keep_going = 'n'


#data = int(input("Enter the integer (0 to quit) :"))
#
#while data !=0:
#    if data > 0:
#        print("That's a positive number..")
#    else:
#        print("That's a negative number...")
#        
#    data = int(input("Enter the integer (0 to quit) :"))
    
    
    
    
#max_temp = 44.33
#temp = float(input("Enter your room temperature : "))
#while temp > max_temp:
#    print("The temperature is too high")
#    print("Turn on your AC and wait")
#    print("15 minute ... Then tale the temperature again and enter your room..")
#    
#    temp = float(input("Enter your room new temperature : "))
#print("The temperature is acceptable")
#print("Check it again in 15 minute")
#    
    
    
# Infinte Loop

keep_going = 'y'

while keep_going == 'y':                                # the condition is tested.
    sales = float(input("Enter the amount of sales"))
    comm_rate = float(input("Enter the commission rate"))
    
    commission = sales * comm_rate
    
    print("The commission is $ ",format(commission ,',.2f'),sep='')
   
#data = 10
#while data < 20:
#    print("Data is less than 20..")