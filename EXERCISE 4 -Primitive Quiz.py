# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:00:15 2024

@author: enzoa
"""

"""In this program, it will ask a question to the user, checks the answer
and provides feedback to the user"""

print ("=============================================")
print ("               PRIMITIVE QUIZ                ")
print ("=============================================")


q1 = input("What is the capital of the country France?(The answer is 'Paris') ")
#This gets the user input as in "Paris"
if q1 == "Paris":
    print ("You got it correct!!")
else:
    print ("Whoops! You got this question wrong!!")
    #if the user inputs anything but "Paris" then this message will show
    
print ("=============================================")
print ("            ADVANCED REQUIREMENT             ")
print ("=============================================")

Q1 = input ("Now, let me repeat, what is the capital of France? ")

if Q1.lower() == "paris": #this lowers the user input to lower case
    print ("Alright, You won this time..")
else:
    print ("HAH YOU GOT IT WRONG!!")
Q2 = input ("Things are just heating up. What is the capital of Albania? ")

if Q2.lower() == "tirana":#this lowers the user input to lower case
    print ("Correct.. You got lucky...")
else:
    print ("WRONGG!! Maybe go back to geography class.")
    
Q3 = input ("What is the capital of Georgia? ")

if Q3.lower() == "tbilisi":#this lowers the user input to lower case
    print ("You're just lucky, correct...")
else:
    print ("Wrong my friend, you may not be good at this.")
    
Q4 =input("What is the Capital of Romania? ")
if Q4.lower() == "bucharest":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")
    
Q5 =input("What is the Capital of Norway? ")
if Q5.lower() == "oslo":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")

Q6 =input("What is the Capital of Wales? ")
if Q6.lower() == "cardiff":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")
    
Q7 =input("What is the Capital of Montenegro? ")
if Q7.lower() == "podgorica":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")
    
Q8 =input("What is the Capital of Croatia? ")
if Q8.lower() == "zagreb":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")
    
Q9 =input("What is the Capital of Latvia? ")
if Q9.lower() == "riga":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")
    
Q10 =input("Last Question. What is the Capital of Liechtenstein? ")
if Q10.lower() == "vaduz":#this lowers the user input to lower case
    print ("You got it correct...")
else:
    print("Wrong, maybe you should get easier questions.")
    
print ("Well you got me beat, that was all of the questions.")