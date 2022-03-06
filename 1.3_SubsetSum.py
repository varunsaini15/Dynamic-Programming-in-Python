import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------SUBSET SUM PROBLEM----------------

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
    # for i in dp:
    #     print(i)               
    return dp[n][Sum]

arr= [ 35, 54, 100, 19, 39, 1, 89, 28, 68, 29, 94 ]
Sum=649
n=len(arr)
print(subsetsum(arr,Sum,n))