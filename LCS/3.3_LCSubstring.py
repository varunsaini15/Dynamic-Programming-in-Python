import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Longest common substring-----------

def lcs(x, y):
    m=len(x)
    n=len(y)
    
    dp=[[None]*(n+1) for i in range(m+1)]
    ans=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                ans=max(ans,dp[i][j])
            else:
                dp[i][j]=0
    return ans
print("Length of LC_substring is ",lcs("abcde","abfce"))