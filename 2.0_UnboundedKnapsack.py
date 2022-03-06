import sys
import math
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------UNBOUNDED KNAPSACK----------------
def Unbounded_knapsack(wt,val,W,n):
    dp=[[0]*(W+1) for i in range(n+1)]            
    for i in range(n+1):
        for j in range(W+1):        
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=W:
                dp[i][j]=max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j]) #only change made in this line 
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][W]
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)
print( Unbounded_knapsack(wt, val, W, n))
