import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Print Longest common subseuqence-----------

def lcs(x,y):
    m=len(x)
    n=len(y)

    dp=[[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp 
def printLcs(x,y):
    m,n=len(x),len(y)
    i,j=m,n 
    ans=""
    dp=lcs(x,y)
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            ans+=x[i-1]
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return ans[::-1]
s1="acbcf"
s2="abcdaf"
print("LCS is ",printLcs(s1,s2))

