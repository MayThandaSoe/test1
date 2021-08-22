# property tax = property value x 0.0065
# Get the first lot number.

#TAX_FACTOR = 0.0065 # Represents the tax factor.
#print('Enter the property lot number')
#print('or enter 0 to end.')
#
##Ask the user at the beginning of the program 
#lot = int(input('Lot number: '))
#
#  # Continue processing as long as the user
#  # does not enter lot number 0.
#while lot != 0:
#    # Get the property value.
#    value = float(input('Enter the property value: '))
#
#    # Calculate the property's tax.
#    tax = value * TAX_FACTOR
#
#    # Display the tax.
#    print('Property tax: $', format(tax, ',.2f'), sep='')
#
#    # Get the next lot number.
#    print('Enter the next lot number or')
##    print('enter 0 to end.')
#    
#    #Ask the user at the end of each loop 
#    lot = int(input('Lot number: '))


# Using a Sentinel loop

##Ask the user at the beginning of the program
#score = int(input("Enter your sccore, use 0 to stop "))
#total = 0
#score_count = 0
#
#while score != 0:
#    total = total + score
#    score_count  = score_count + 1
##Ask the user at the end of each loop
#    score = int(input("Enter your sccore, use 0 to stop "))
#
#print("The total test score is " , total)
#print("The average test score is " , total/score_count)

# Displays the seconds from 0 to 59:
#for seconds in range(60):
#    print(seconds)
##    
#for minutes in range(60): # 0 
#    for seconds in range(60): # 60
#        print(minutes, ':', seconds)
##    
#for hours in range(24):              # 0 to 23
#    for minutes in range(60):        # 0 to 59
#        for seconds in range(60):    # 0 to 59
#           print(hours, ':', minutes, ':', seconds)


# This program averages test score and asks the user for the number of students
# and the number of test score....

 #Get the number of students.
#num_students = int(input('How many students do you have? '))
# 
# #Get the number of test scores per student.
#num_test_scores = int(input('How many test scores per student? '))
# 
# #Determine each student's average test score.
#for student in range(num_students): # 0 to 2
#     # Initialize an accumulator for test scores.
#    total = 0.0
#    # Get a student's test scores.
#    # print(student).....0
#    print('Student number', student + 1)
#    print('–––––––––––––––––')
#    for test_num in range(num_test_scores):  # 0 to 3
#        print('Test number', test_num + 1, end='')
#        score = float(input(': '))
#       # Add the score to the accumulator.
#        total += score
#
#    # Calculate the average test score for this student.
#    average = total / num_test_scores
#
#     # Display the average.
#    print('The average for student number', student + 1, 
#           'is:', average)
#    print()
# 
