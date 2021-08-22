# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:17:28 2020

@author: Mahendra
"""



# import pickle
# import contact

# LOOK_UP =1
# ADD =2
# CHANGE = 3
# DELETE = 4
# QUIT = 5

# FILENAME = 'contacts.dat'



# def main():
#     my_contacts = load_contacts()
    
    
  
#     choice = 0
    
#     while choice != QUIT:
#         choice = get_menu_choice()
#         if choice == LOOK_UP:
#             look_up(my_contacts)
#         elif choice ==ADD:
#             add(my_contacts)
#         elif choice == CHANGE:
#             change(my_contacts)
#         elif choice == DELETE:
#             delete(my_contacts)
            
#     save_contacts(my_contacts)
    
    
# def load_contacts():
#     try:
#         input_file = open(FILENAME,'wb')
        
#         contact_dict= pickle.load(input_file)
#         input_file.close()
        
#     except IOError:
#         contact_dict ={}
        
        
#     return contact_dict

# def get_menu_choice():
#     print()
#     print("Menu")
#     print("-------------------------")
#     print("1. look up a contact")
#     print("2. Add a contact")
#     print("3. Change the contact")
#     print("4. Delete the contact")
#     print("5.Quit")
#     print()
    
#     choice = input("Enter a valid choice")
    
#     while choice < LOOK_UP or choice > QUIT:
#         choice =input("Enter a valid choice")
       
     
    
#     return choice


def look_up(my_contacts):
    
    name = input("Enter a name")
    print(my_contacts.get(name,"The name is not found"))
    
    
# def add(my_contacts):
#     name = input("Enter a name")
#     phone = input("Enter phone number ")
#     email= input("Enter an email")
    
#     entry = contact.Contact(name,phone,email)
    
#     if name not in my_contacts:
#         my_contacts[name] = entry
#     else:
#         print("The name is already exist..")
        
# def change(my_contacts):
#     name = input("Enter a name ")
#     if name in my_contacts:
#         phone = input("Enter a phone number")
#         email = input("Enter an email")
#         entry = contact.Contact(name,phone,email)
#         my_contacts[name] = entry
#         print("The information has been updated..")
        
#     else:
#         print("The name is not found....")
        
        
# def delete(my_contacts):
#     name = input("Enter a name")
    
#     if name in my_contacts:
#         del my_contacts[name]
#         print("Entry deleted..")
        
#     else:
#         print("The name is not found...")
        
        
# def save_contacts(my_contacts):
#     output_file = open(FILENAME,'wb')
    
#     pickle.dump(my_contacts,output_file)
    
#     output_file.close()
    
# main()

        
# dictionary.get(keyname, value)
   
        
my_contacts = {"Aung Aung" : "19",
               "Mya Mya" : 20,
               "Zaw Zaw " : 30}

print(my_contacts.get("Aung Aung"))

print(my_contacts.get("Kyaw Kyaw",234))

print(my_contacts.get("Aye Aye"))

    
            
            
            
    
    

