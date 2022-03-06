import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------MEMOISATION----------------
'''
INPUT: 
10 20 30
60 100 120
50
Output:
220
'''
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
W=int(input())
n=len(wt)
    
dp=[[-1]*(W+1) for i in range(n+1)]
def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if dp[n][W]!=-1:
        return dp[n][W]
    if wt[n-1]<=W:
        dp[n][W]=max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        return dp[n][W]
    elif wt[n-1]>W:
        dp[n][W]=knapsack(wt,val,W,n-1)
        return dp[n][W]
print("Maximum Profit is =",knapsack(wt,val,W,n))
