# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 01:21:19 2024

@author: enzoa
"""
"""This block of code is used to show how to utilize dictionaries"""
print ('''           ======================
                                 
                 EXERCISE 3      
                 BIOGRAPHY       
                                 
           ======================''')
Personal_info = {
    "name:" : "Enzo",
    "age:" : 18,
    "Hometown:" : "Dubai"
    }
for key, value in Personal_info.items():
    print (key, value)
    """ This utilizes items() to garher the key value pairs
    from the dictionary, the for loop help to iterate each pair, then this prints
    the key value pairs on separate lines."""
    
print ("======================")   
print ("ADVANCED REQUIREMENT")
print ("======================")

    



while True:
    name = input("Enter your first name: ") #asks the user to input their FIRST name
    wordcount1 = len(name.split()) #This code splits the string into multiple words when there is a space
    if wordcount1 > 1:
        print ("You have entered more than your first name")
        print ("Re-enter your name")
        continue
    else:
        break
"""The while loop checks the word count if it is higher than one word, if
        it is then it will continue to ask the user to re enter their name with
        only ONE word , it will keep asking until the user enters their first name
        then the loop breaks"""
        


while True:
    try:
        age = int(input("Enter your age: "))
        break
    except:
        print ("These are words, enter your real age")
        
'''This catches an error in the try-except block, the error being the ValueError
and prints a message to re-enter the correct value and will keep asking until
the user enters the desired data'''

    
hometown = input("Enter your hometown: ")

print ("Your name is ", name)
print ("Your age is ", age)
print ("Your hometown is ", hometown)