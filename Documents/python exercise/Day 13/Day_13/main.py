# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:11:45 2020

@author: Mahendra
"""

"""
Writing Data to file

"""

# def main():
#     # Open
#     output_file = open("name.txt",'w')
    
#     # Process
#     output_file.write("Aung Aung\n")
#     output_file.write("Su Su\n")
#     output_file.write("Mya Mya\n")
#     output_file.write('*******************')
    
#     #close
#     output_file.close()
    
# main()

"""
Reading Data from file

"""

# def main():
#     infile = open("name.txt",'r')
    
#     file_contents = infile.read()
    
#     infile.close()
    
#     print(file_contents)
    
# main()

# def main():
#     infile = open("name.txt",'r')
    
#     line1 = infile.readline()
#     line2 = infile.readline()
#     line3 = infile.readline()
#     line4 = infile.readline()
    
#     infile.close()
    
#     print(line1)
#     print(line2)
#     print(line3)
#     print(line4)
    
# main()



"""
 Concatenating a Newline to a String

"""
# def main():
#     name1 = str(input("Enter your name"))
#     name2 = str(input("Enter your friend name"))
#     name3 = str(input("Enter your other friend name"))
    
#     myfile = open("friends.doc",'w')
    
#     myfile.write(name1 + '\n')
#     myfile.write(name2 + '\n')
#     myfile.write(name3 + '\n')
    
#     myfile.close()
    
# main()

# def main():
#     infile = open("friends.doc",'r')
    
#     line1 = infile.readline()
#     line2 = infile.readline()
#     line3 = infile.readline()



#     line1 = line1.rstrip('\n')
#     line2 = line2.rstrip('\n')
#     line3 = line3.rstrip('\n')
    
#     infile.close()
    
#     print(line1)
#     print(line2)
#     print(line3)
    
# main()

"""
Returns a copy of the string with trailing characters removed.
"""

# mystring = "Aung Aung and Mya Myaaaab"
# test = mystring.rstrip('ab')
# print(test)


"""
Appending datat to an existing file

"""
# def main():
#     myfile = open("friends.doc",'a')
    
#     myfile.write("Myo Arkar\n")
#     myfile.write("Su Myat\n")
#     myfile.write("Aye Aye\n")
#     myfile.write("Kyaw Aung\n")
        
#     myfile.close()

# main()    

"""
Writing and Reading Numeric Data
"""

# def main():
#     outfile = open("numbers.txt",'w')
    
#     num1 = int(input("Enter a number"))
#     num2 = int(input("Enter a number 2"))
#     num3 = int(input("Enter a number 3"))

#     outfile.write(str(num1) + '\n')
#     outfile.write(str(num2) + '\n')
#     outfile.write(str(num3) + '\n')
    
#     outfile.close()
    
#     print("Data written to numbers.txt")
    
# main()
    
    
# def main():
#     infile = open("numbers.txt",'r')
    
#     num1 = int(infile.readline())
#     num2 = int(infile.readline())
#     num3 = int(infile.readline())

#     infile.close()
    
#     total =( num1 * num2) * num3
#     print("The numbers are ",num1 ,num2 ,num3)
#     print("The total value is",total)
    
# main()


"""
Using for loop in file Processing
"""

# def main():
#     days = int(input("For how many days do " +
#                      'you have sales?'))
    
#     sale_file = open("sales.txt",'w')
    
#     for count in range(1,days + 1):
#         sales = float(input("Enter the sales for day #" +
#                             str(count) + ':'))
        
#         sale_file.write(str(sales) + '\n')
        
#     sale_file.close()

# main()

def main():
    sales_file = open('sales.txt','r')
    
    line = sales_file.readline()  
    # readline() also detects EOF..end of file
    # line = ""
    
    while line!= '':
        amount= float(line)
        print(format(amount,'.2f'))
        line = sales_file.readline()
    sales_file.close()

main()