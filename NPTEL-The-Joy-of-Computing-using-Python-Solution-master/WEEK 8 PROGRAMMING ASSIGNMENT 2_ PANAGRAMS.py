"""QUESTION 
A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES

SOLUTION"""

alphabet=[]
for i in range(97,123):
    alphabet.append(chr(i))
s=input()
s=s.lower()
d=set(s)
d=list(d)
for i in d:
    if i in alphabet:
        alphabet.remove(i)
if len(alphabet)==0:
  print("YES",end="")
else:
  print("NO",end="")
