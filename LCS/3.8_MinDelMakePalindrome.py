import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#--------Min no of deletions to make string palindrome-----1312 leetcode hard-----
def lcs(x,y):
    m=n=len(x)
    dp=[[0]*(n+1) for _ in range(n+1)]            
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]
s="agbcba"
if s==s[::-1]:
    print(0)
else:
    print(len(s)-lcs(s,s[::-1]))
# Same code for min insertion to make string palindrome