import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Palindrome partioning memoised-----------
def isPalin(t):
    return t==t[::-1]
def solve(s,i,j):
    if i>=j or isPalin(s[i:j+1]):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    ans=math.inf
    for k in range(i,j):
        tmp_ans=solve(s,i,k)+solve(s,k+1,j)+1
        ans=min(ans,tmp_ans)
    dp[i][j]=ans
    return ans 

s="ababbbabbababa"
n=len(s)
dp=[[-1]*(n+1) for i in range(n+1)]
print("Min no. partitions=",solve(s,0,n-1))
#---------Palindrome partioning memoised optimized-----------
# def isPalin(t):
#     return t==t[::-1]
# def solve(s,i,j):
#     if i>=j or isPalin(s[i:j+1]):
#         return 0
#     if dp[i][j] != -1:
#         return dp[i][j]
#     ans=math.inf
#     for k in range(i,j):
#         tmp_ans=solve(s,i,k)+solve(s,k+1,j)+1
#         ans=min(ans,tmp_ans)
#     dp[i][j]=ans
#     return ans 

# s="ababbbabbababa"
# n=len(s)
# dp=[[-1]*(n+1) for i in range(n+1)]
# print("Min no. partitions=",solve(s,0,n-1))