"""QUESTION

Given a square matrix of N rows and columns, find out whether it is symmetric or not.

Input Format:
The first line of the input contains an integer number n which represents the number of rows and the number of columns.
From the second line, take n lines input with each line containing n integer elements with each element separated by a space.

Output Format:
Print 'YES' if it is symmetric otherwise 'NO'

Example:

Input:
2
1 2
2 1

Output:
YES

SOLUTION"""

n=int(input())
l=[]
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        l.append(temp)
#UPLOADED BY ULTIMATE GAMER
x=0
for i in range(n):
    for j in range(n):
        if l[i][j]!=l[j][i]:
           x=x+1
if x==0:
  print("YES",end="")
else:
  print("NO",end="")
