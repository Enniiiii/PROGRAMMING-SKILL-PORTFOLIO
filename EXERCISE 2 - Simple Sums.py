# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 01:18:01 2024

@author: enzoa
"""
"""This program shows how integer variables work and how the result is printed"""

while True: #checks if the user has entered an integer
    try:
        a = int (input ("Enter your first number: ")) #Gets the first input
    except:
        print ("Please re-enter as a number.")
        continue
    else:
        break

while True:#checks if the user has entered an integer
    try:
        b = int(input ("Enter your second number:")) #Gets the second input
    except:
           print ("Please re-enter as a number.")
           continue
    else:
        break
        
c = a + b
print (f"Your answer is {c}") 
"""a and b variables store values, c stores the result
and this shows the result of the sum"""