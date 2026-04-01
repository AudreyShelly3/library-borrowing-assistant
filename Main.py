# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:21:00 2026

@author: Takunda Mhenyu
"""
#Library Membership & Resource Management System
#Scenario 1: A single Member Borrowing Assistant

#Display Welcome Message
print("Welcome to the Library Memmbership and Resource Management System \n")

#Create a dictionary to store member details
member_details = {}

#Create a list to store borrowed items
#Each borrowed item will be stored as a dictionary
borrowed_items = []

#Create a variable choice as the menu
choice = ""

#Collect member personal details from the user
print("\nPlease enter your personal details")

member_details["name"] = input("Enter your name: ")
member_details["birthdate"] = input("Enter your day of birth: ")
member_details["email"] = input("Enter your email address: ")
member_details["mobile"] = input("Enter your mobile number: ")

print("\nMember details saved successfully!")

#Main program loop
#This loop keeps the program running until user selects exit
while choice != "6":
    #Display menu option
    print ("\n==========  MAIN MENU  =========")
    print("1. View member details")
    print("2. Add borrowed item")
    print("3. View borrowed item")
    print("4. View items grouped by due date")
    print("5. Mark item as returned")
    print("6. Exit")
    
    #Ask user to enter a menu choice
    choice = input("Enter your choice: ")
    
    #option 1: view member details
    if choice == "1":
        print("\n------  Member Details  ------")
        print("Name:",member_details["name"])
        print("Birthdate:", member_details["birthdate"])
        print("Email:", member_details["email"])
        print("Mobile:",member_details["mobile"])
        
    #option 2: add borrowed item
    elif choice == "2":
        print("\n-----  Add Borrowed item  ----")
        
        #create a dictionary to store one borrowed item
        item ={}
        
        #collect item information from the user
        item["title"]=input("Enter item title: ")
        item["type"]=input("Enter item type (book, DVD etc): ")
        item["borrowed_date"]=input("Enter borrowed date: ")
        item["due_date"]=input("Enter due date: ")
        
        #set default returned status to no
        item["returned"]= "No"
        
        #add the item dictionary to the borrowed_items list
        borrowed_items.append(item)
        
        print("Item added successfully!")
    
    #option 3: View all Borrowed items
    elif choice == "3":
        print("\n------  Borrowed Items  ------")
        
        #check if the borrowed items list is empty
        if len(borrowed_items) == 0:
            print("No borrowed items recorded.")
        else:
            #create counter variable for while loop
            i = 0
            
            #loop through borrowed_items list
            while i < len(borrowed_items):
             print("\nItem Number:", i + 1)
             print("Title:", borrowed_items[i]["title"])
             print("Type:", borrowed_items[i]["type"])
             print("Borrowed Date:", borrowed_items[i]["borrowed_date"])
             print("Due Date:", borrowed_items[i]["due_date"])
             print("Returned:", borrowed_items[i]["returned"])
             
             #increase the counter
             i = i+1
    #option 4: View items grouped by due date
    elif choice == "4":
        print("\n--- Items Grouped by Due Date ---")
        
        # Check if there are items in the list
        if len(borrowed_items) == 0:
           print("No borrowed items available.")
        else: 
            #Create dictionary to group items by due date
            grouped_due_dates = {}
            i = 0
            
            #loop through borrowed items
            while i < len(borrowed_items):
                
              # Get due date of the current item
              due = borrowed_items[i]["due_date"]
              
              # If due date does not exist in dictionary create new list
              if due not in grouped_due_dates:
               grouped_due_dates[due] = []
               
              #add item title to that due date group
              grouped_due_dates[due].append(borrowed_items[i]["title"])
              i = i + 1
              
            #Get list of due dates
            due_dates = list(grouped_due_dates.keys())
            j = 0
             
            #Loop through grouped due dates
            while j < len(due_dates):
                print("\nDue Date:", due_dates[j])
                
                k = 0
                
                #Loop through items under that due date
                while k < len(grouped_due_dates[due_dates[j]]):
                    print("-", grouped_due_dates[due_dates[j]][k])
                    k = k + 1
                j = j + 1
    #option 5: Mark item as returned
    elif choice == "5":
     print("\n-----  Borrowed Items  -----\n")
     
     
     #Check if borrowed items exist
     if len(borrowed_items) == 0:
         print("No borrowed items available.")
     else:
        i = 0
        
        #Display all borrowed items 
        while i < len(borrowed_items):
            
            print(
                    str(i + 1) + ". " +
                    borrowed_items[i]["title"] +
                    " | Due: " + borrowed_items[i]["due_date"] +
                    " | Returned: " + borrowed_items[i]["returned"]
                    )
            i = i + 1
         
         #After displaying items, ask the user which one to return
        print("\nSelect which item you want to mark as returned")
        item_number = input("Enter item number: ")
         
        #Check if input is a number
        if item_number.isdigit():
             index = int(item_number) - 1
             
             #Check if number is valid
             if index >= 0 and index < len(borrowed_items):
                #Mark the item as returned 
                borrowed_items[index]["returned"] = "Yes"
                print("Item marked as returned.")
             else:
                 print("Invalid item number.")
        else:
            print("Please enter a valid number.")
    #option 6: Exit program
    elif choice == "6":
        print("\nThank you for using the system. \nGoodbye!")
        
        #If user enters invalid menu option
    else:
        print("Invalid choice. Please try again.")

