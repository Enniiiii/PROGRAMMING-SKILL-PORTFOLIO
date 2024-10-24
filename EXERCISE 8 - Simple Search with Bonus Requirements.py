# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:21:18 2024

@author: enzoa
"""
"""This Program will help to search a specific string within a list of strings"""
print ("=============================================")
print ("               SIMPLE SEARCH                 ")
print ("=============================================")

myList = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

print (myList[4]) #prints the fifth string being sam since indexes start from 0

print ("======================")   
print ("OPTIONAL REQUIREMENT")
print ("======================")

print (myList)
while True:
    try: #checks if the user has inputted the position of the desired name
        inputName = int(input ("Please enter the number corresponding to the position: "))
    except:
            print ("Please Re-enter the position number.")
            continue
    if inputName <1 or inputName >6:
        print ("Please enter between 1 - 6") #Checks if 1 - 6 is entered
        continue
    else:
        break

#prints the name of the person the user is searching
print (f"The name searched is {myList[inputName-1]}")