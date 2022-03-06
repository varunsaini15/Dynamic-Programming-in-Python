import sys
import math
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Minimum subset sum difference----------------
def subsetsum(arr,Sum,n):
    dp=[[False]*(Sum+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,Sum+1):
        dp[0][i]=False
    for i in range(1,n+1):
        for j in range(1,Sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n]

arr=[1,2,7]
n=len(arr)
Range=sum(arr)
l=subsetsum(arr,Range,n)
mn=math.inf
for i in range(len(l)//2):
    if l[i]==True:
        # print(i)
        mn=min( mn , Range- 2*i )
print("Minimum subset sum difference is :",mn)

# for some reason doesnt work if -ve numbers in the array.
