import sys
import math
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Coin change 2 Problem----------------
def coinChange(coins,amount):
    n=len(coins)
    dp=[[math.inf -1]*(amount+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    i=1
    for j in range(1,amount+1):
        if j%coins[0]==0:
            dp[i][j]=j//coins[0]
        else:
            dp[i][j]=math.inf-1
    for i in range(2,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    if dp[-1][-1] == math.inf:
        return -1
    return dp[-1][-1]
coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))

    