import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------------------
'''
Problem: find the sum of first N numbers

Objective function:
f(i) is the sum of first i elements

Recurrence relation:
f(n) = f(n-1) + n

'''

def nsum(n):
    dp=[0]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        dp[i]=dp[i-1]+i
    print(dp)
    return dp[n]

print(nsum(5)) 
print(nsum(10))




