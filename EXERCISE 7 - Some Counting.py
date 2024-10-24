# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:40:23 2024

@author: enzoa
"""
"""This program will show how to utilize loops to accomplish different tasks"""

print ("=============================================")
print ("              SOME COUNTING                  ")
print ("=============================================")

print ("LOOP ONE:") #counts from 0 - 50 in increments of 1
loopNum = 0
print (loopNum)
while True:
    loopNum +=1
    print (loopNum)
    if loopNum == 50:
        break

print ("LOOP TWO:") #counts from 50 - 0 in decrements of -1

while True:
    loopNum == 50
    loopNum -= 1
    print (loopNum)
    if loopNum == 0:
        break
    
print ("LOOP THREE:") #counts from 30 -50 in increments of 1

loopNum2 = 30
print (loopNum2)
while True:
    loopNum2 += 1
    print (loopNum2)
    if loopNum2 == 50:
        break

print ("LOOP FOUR:") #counts from 50 to 10 in decrements of 2
loopNum3 = 50
print (loopNum3)
while True:
    loopNum3 -= 2
    print (loopNum3)
    if loopNum3 == 10:
        break
    
print ("LOOP FIVE:") #counts from 100 - 200 in increments of 5
loopNum4 = 100
while True:
    loopNum4 += 5
    print (loopNum4)
    if loopNum4 == 200:
        break