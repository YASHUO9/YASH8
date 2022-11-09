# This program i have run to find the reverse of the stack using one more as empty and recursion as the build in stack

def reverseStack(s1,s2):
    if (len(s1) <= 1):
        return
    while (len(s1)!=1):
        ele = s1.pop()
        s2.append(ele)
    lastElement = s1.pop()
    
    while (len(s2)!=0):
        ele = s2.pop()
        s1.append(ele)
        
    reverseStack(s1,s2)
    s1.append(lastElement)
    
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [ int(ele) for ele in input().split()]
s2 =[]
while (len(s1) !=0):
    print(s1.pop(),end = '')
reverseStack(s1,s2)
while (len(s1) !=0):
    print(s1.pop(),end = '')