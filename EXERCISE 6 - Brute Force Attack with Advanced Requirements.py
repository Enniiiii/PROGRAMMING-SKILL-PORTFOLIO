# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:49:03 2024

@author: enzoa
"""

"""The program is a password entry system, the correct password is 12345,
this program should ask the user to repeatedly enter the password until the correct
one is entered"""

print ("=============================================")
print ("            BRUTE FORCE ATTACK               ")
print ("=============================================")

correctPassWord = "12345"
incorrectAttempts = 5

while True: #while loop that checks if the user entered the correct password
    passInput = input ("Enter your Password (12345): ")
    if passInput == "12345":
        print ("That is the correct password")
        break
    else: #ADVANCED REQUIREMENT, shows the amount of attempts left for the user
        print (f"Incorrect Password,You have {incorrectAttempts} attempts left, Re-enter the password")
        incorrectAttempts -= 1
        if incorrectAttempts < 0:
            print ("The authorities have been alerted, enjoy")
            break
        continue
    
'''The while loop keeps looping until the user has entered the correct password
or until the user has used up all of their attempts'''
        
