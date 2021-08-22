# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:16:56 2020

@author: Mahendra
"""


"""

The area of circle
The circumference of circle
The area of rectangle
The perimeter of a rectangle

"""

import circle
import rectangle

# Constant for the menu choices

area_circle_choice = 1
circumference_circle_choice = 2
area_rectangle_choice = 3
perimeter_rectangle_chioice = 4
quit_choice = 5

def main():
    choice = 0
    
    while choice != quit_choice:
        # Display the menu
        display_menu()
        choice = int(input("Enter your choice"))
        
        if choice == area_circle_choice:
            radius = float(input("Enter the circle's radius :"))
            print("The area is ",circle.area(radius))
            
        elif choice == circumference_circle_choice:
             radius = float(input("Enter the circle's radius :"))
             print("The Circumference is ",circle.circumference(radius))
             
             
        elif choice == area_rectangle_choice:
             width = float(input("Enter the rectangle's width :"))
             length = float(input("Enter the rectangle's length :"))
             print("The area is ",rectangle.area(width,length))
             
        elif choice == perimeter_rectangle_chioice:
             width = float(input("Enter the rectangle's width :"))
             length = float(input("Enter the rectangle's length :"))
             print("The Perimeter is ",rectangle.perimeter(width,length))
             
        elif choice == quit_choice:
            print("Existing the program.......")
            
        else:
            print("Error")
                      
def display_menu():
    print("Menu")
    print("(1)  Area of Circle")
    print("(2)  Circumference of Circle")
    print("(3)  Area of Rectangle")
    print("(4)  Perimeter of Rectangle")
    print("(5)  Quit")
    
main()
    