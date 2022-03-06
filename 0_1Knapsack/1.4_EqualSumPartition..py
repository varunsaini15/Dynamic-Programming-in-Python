import re
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Equal Sum Partition----------------

def subsetsum(arr,Sum,n):
    dp=[[False]*(Sum+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for j in range(1,Sum+1):
        dp[0][j]=False
    for i in range(1,n+1):
        for j in range(1,Sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][Sum]

def equalsumpartition(arr,n):
    s=sum(arr)
    if s%2!=0:
        return False
    else:
        return subsetsum(arr,s//2,n)


arr = [1,5,11,5]
n=len(arr)
print(equalsumpartition(arr,n))
