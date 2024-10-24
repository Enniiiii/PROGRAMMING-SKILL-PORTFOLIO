# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:20:39 2024

@author: enzoa
"""

"""This program should tell the user how many days are there in a specific month
, this uses a dictionary for the month numbers and its corresponding days"""

print ("=============================================")
print ("             DAYS OF THE MONTH               ")
print ("=============================================")

Months = { #Dictionary where the key is the month num, then value is the days
    1 :["January", 31], #This Dictionary utilizes a 3D array (a list within a dictionary)
    2 :["February", 28],
    3: ["March", 31],
    4: ["April", 30],
    5:["May", 31],
    6:["June", 30],
    7:["July", 31],
    8:["August", 31],
    9:["September", 30],
    10:["October", 31],
    11:["November", 30],
    12:["December", 31]
 }


# Converts dictionary values to a list
monthValues = list(Months.values()) 

while True:
    try:
        Mnum = int( input ("Please enter the month (1-12): "))
    except:
        print("Please input numbers only") #Checks if only integers are entered
        continue 
    
    if Mnum <1 or Mnum >12:
        print ("Please enter between 1 - 12") #Checks if 1 - 12 is entered
        continue
    else:
        break

for i in Months.keys():
    #ADVANCED REQUIREMENT to account for leap year
    if Mnum == 2:
        askInput = input("Is it a Leap year? (Y/N) ").lower()    
        if askInput == "y":
            print ("February has 29 days.")
        elif askInput == "n":
            print (f"{monthValues[2-1][0]} has {monthValues[2-1][1]} days.")
        else:
            print ("Please Re-enter Y or N")
            continue
        break

    if Mnum == i:
        print(f"{monthValues[i-1][0]} has {monthValues[i-1][1]} days.")
        
'''This takes the index of each key-value and shows the amount days accordingly
to the month (the index is minus 1 to since the index starts at 0)'''

'''The advanced requirement accounts for leap year, if the user enters 2 for 
februrary, they are prompted to ask if its a leap year (the answers are
   automatically lowercased), otherwise if it is another response, the program
will repeat to ask to enter the Y or N'''

