import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------------------
'''
prob: climbing stairs

1. Objective function:
    f(i) is no. of distinct ways to reach the top
2. Identify base cases
    f(0)=1
    f(1)=1
3. Recurrence relation
    f(n)=f(n-1)+f(n-2)
4. Order of computation
    Bottom-up
5. Answer will be in f(n)

'''
#Time complexity: O(n)
#Space complexity: O(n)
def climbStairs(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]

print(climbStairs(5))