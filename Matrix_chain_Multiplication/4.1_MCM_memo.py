import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Matrix Chain Multiplication Memoisation-----------
def solve(arr,i,j):
    if i>=j:
        return 0
    ans=math.inf
    if dp[i][j] != -1:
        return dp[i][j]

    for k in range(i,(j-1)+1):
        cost=arr[i-1]*arr[j]*arr[k]
        tmp_ans=solve(arr,i,k)+solve(arr,k+1,j)+cost 
        ans=min(ans,tmp_ans)
    dp[i][j]=ans
    return ans

arr=[40,20,30,10,30]
n=len(arr)
dp=[[-1]*(n+1) for i in range(n+1)]
print("Min cost is",solve(arr,1,n-1))
