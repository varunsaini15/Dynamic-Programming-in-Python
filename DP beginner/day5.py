from cmath import cos
import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#--------------------------------
'''
OPTIMIZATION PROBLEM
-------------------------------------
Problem:
minimum steps in climbing stairs
'''
def paidStaricase(n,cost):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=cost[1]
    for i in range(2,n+1):
        dp[i]=cost[i]+min(dp[i-1],dp[i-2])
    print(dp)
    return dp[n]

cost=[0,10,15,20]
print(paidStaricase(3,cost))
