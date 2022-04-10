import sys
import math
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Coin change 1 Problem----------------
def change(amount,coins):
    n=len(coins)
    dp=[[0]*(amount+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for j in range(amount+1):
        dp[0][j]=0
    for i in dp:(print(i))
    for i in range(1,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]

amount = 5
coins = [1,2,5]
print(change(amount,coins))                