import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Count SUBSET SUM PROBLEM----------------

def Countsubsetsum(arr,Sum,n):
    dp=[[0]*(Sum+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for j in range(1,Sum+1):
        dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,Sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    # for i in dp:
    #     print(i)               
    return dp[n][Sum]

arr= [ 2,3,5,6,7,10 ]
Sum=10
n=len(arr)
print(Countsubsetsum(arr,Sum,n))