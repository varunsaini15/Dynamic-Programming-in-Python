import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Shortest common subseuqence-----------
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
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

def ShortestCommonSupersequence(x,y):
    return len(x)+len(y)-lcs(x,y)

X = "AGGTAB"
Y = "GXTXAYB"
print("length is",ShortestCommonSupersequence(X,Y))
