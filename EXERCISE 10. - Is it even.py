# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:29:16 2024

@author: enzoa
"""

"""Write a program that checks if the value entered is odd or even"""

    

def evenOrOdd(num): #this function checks if the number is even or odd
    if num % 2 == 0:
        print (f"The number {num} is even")
    else:
        print (f"The number {num} is odd")
        
        
def main(): #This asks for the user to input their number then the evenOrOdd function is called to check the inputted number
    while True:
        try:
            numInput = int(input("Enter your number: "))
            break
        except: #Checks if the user has entered an invalid input such as string
            print ("That is text. Please Re-enter your number.")
            
    numResult = evenOrOdd(numInput)
    print (numResult)
    
if __name__ == "__main__":
    main()
