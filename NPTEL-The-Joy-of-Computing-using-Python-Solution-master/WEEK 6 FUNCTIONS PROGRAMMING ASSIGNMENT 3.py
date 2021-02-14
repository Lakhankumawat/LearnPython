"""QUESTION
Given an integer number n, define a function named printDict() which can print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys.
The function printDict() doesn't take any argument.

Input Format:
The first line contains the number n.

Output Format:
Print the dictionary in one line.

Example:

Input:
5

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

NOTE: You are supposed to write the code for the function printDict() only. The function has already been called in the main part of the code.

SOLUTION"""

def printDict():
  x=int(input())
  #uploaded by ULTIMATE GAMERGG
  d={}
  for i in range(x):
    d[i+1]=(i+1)**2
  print(d,end='') 
printDict()
printDict()
