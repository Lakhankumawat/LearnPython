"""QUESTION
Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.

Input Format:

A number n.

Output Format:

Print the factorial of n.

Example:

Input:
4

Output:
24


SOLUTION"""

x=int(input())
s=1
for i in range(x,0,-1):
   s=s*i
print(s,end="")
