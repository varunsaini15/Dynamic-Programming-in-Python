import sys
import math
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Rod Cutting Problem----------------
def rodcutting(length,price,N,n):
    dp=[[0]*(N+1) for i in range(n+1)]            
    for i in range(n+1):
        for j in range(N+1):        
            if i==0 or j==0:
                dp[i][j]=0
            elif length[i-1]<=N:
                dp[i][j]=max(price[i-1]+dp[i][j-length[i-1]],dp[i-1][j]) #only change made in this line 
            else:
                dp[i][j]=dp[i-1][j]
    for i in dp:
        print(i)
    return dp[n][N]
N = 8
price = [1, 5, 8, 9, 10, 17, 17, 20 ]
length = [1,2,3,4,5,6,7,8]
n = len(price)
print( rodcutting(length, price, N, n))
