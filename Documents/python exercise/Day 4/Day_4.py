# Inserting Comma Separators
#print(format(12454443333456.544,',.2f'))

# Scientific Notation
#print(format(12343.3543,'.2e'))

#monthly_pay = 10000.0
#annual_pay = monthly_pay * 12
#print("Your annual pay is $ ",\
#      format(annual_pay,',.2f'),\
#      sep='')

# Homework
#num1=127.8995464
#num2=3456.35345645
#num3=5.34345645
#num4=45453.343345646
#
#print(format(num1,',.2f'))

# Floating point number as percantage

#print(format(0.5,'%'))
#
#print(format(0.5,'.0%')) # specific 0 as the precision


# formatting integer
#print(format(12242233,'d'))
#print(format(12242233,',d'))    # comma serparator
#print(format(12,'8d'))          # 8 space wide

# name constant

#monthly_pay = 10000.0
#count = 15
##annual_pay = monthly_pay *  15
#monthly_pay =float(input("Enter your salary.."))
#mgmg_annual_pay = monthly_pay *  count
#
#monthly_pay =float(input("Enter your salary.."))
#kyawkyaw_annual_pay = monthly_pay *  count
#
#annual_pay = monthly_pay *  12
#print("Your annual pay is $ ",\
#      format(annual_pay,',.2f'),\
#      sep='')


#apple = 10  # assignment symbol (is assigned )
#x=1
#if x==10:# relational operator (is equal to )
#    print("TRUE")
#else:
#    print("FALSE")

#num1= int(input ("Enter first integer"))
#num2 = int(input("Enter second integer"))
#num3 = int(input("Ënter third integer"))
#
#minimum = num1
#
#
#if num2 < minimum:
#    minimum = num2
#if num3 < minimum:
#    minimum = num3
#
#print("Minimum Value" , minimum)

#max_grades = 70
#grades= int(input("Enter your marks"))
#
#if grades >= max_grades:
#    print("Passed")
#    
#else:
#    print("Failed")
#    
    
#sales = 5000
#max_sales = int(input("Enter your sales amount"))
#if max_sales >= sales:
#    print("You met your sales quota..")
#else:
#    print("False")

#highest_score = 95
#total_sub = 3
#sub_1 = int(input("Enter your marks"))
#sub_2 = int(input("Enter your marks"))
#sub_3 = int(input("Enter your marks"))
#
#average = (sub_1 + sub_2 + sub_3) / total_sub
#
#if average >= highest_score: # Is average greater than or equal to highest_score?
#    print("Passed")
#    print("Average Marks",average)
#else:
#    print("Failed")

#temperature = int(input("Enter your room temperature"))

## temperature != 30 ..boolean expression
#if temperature != 30: # Is temperature is not equal to 30?
#    print("Temperature is ",temperature)
#else:
#    print("Error")

#if temperature == 30:
#    print("Temperature is ",temperature)
#else:
#    print("Error")


#max_grades = 70
#grades= int(input("Enter your marks"))
#
#if grades >= max_grades:
#    print("Passed")
#    
#else:
#    print("Failed")
#    print("You must take this course again..")


# If student's grade is greater than or equal to 90
    # Display "A"
# Else if student's grade is greater than or equal to 80
    # Display "B"
# Else if student's grade is greater than or equal to 70
    # Display "C"
# Else if student's grade is greater than or equal to 60
    # Display "D"
# Else if student's grade is greater than or equal to 50
    # Display "E"


#grade = int(input("Enter your marks.. "))
#
#if grade >= 90:
#    print("Grade A")
#elif grade >= 80:
#    print("Grade B")
#elif grade >= 70:
#    print("Grade C")
#elif grade >= 60:
#    print("Grade D")
#elif grade >= 50:
#    print("Grade E")
#else:
#    print("FAILED")


# If the employee worked more than 40 hours:
    # Calculate and display the gross pay with overtime
# Else :
    # Calculate and display the gross pay
    
#base_hour = 40 # base hour per week
#overtime_multiplier = 1.5 # overtime multipler
#
#hours = int(input("Enter the number of hour worked : "))
#pay_rate = float(input("Enter the hourly pay rate : "))
#
#if hours > base_hour:
#    overtime= hours - base_hour
#    overtime_payment = overtime_multiplier * pay_rate * overtime
#    gross_pay =  (base_hour*pay_rate) +  overtime_payment
#    
#else:
#    gross_pay =  base_hour*pay_rate
#    
#print("The gross pay is $ ",format(gross_pay,',.2f'),sep='')
    

