import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Print Shortest common subseuqence-----1092 Leetcode hard------
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
    return dp

def printScs(x,y):
    i=m=len(x)
    j=n=len(y)
    s=''
    dp=lcs(x,y)
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            s+=x[i-1]
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                s+=x[i-1]
                i-=1
            else:
                s+=y[j-1]
                j-=1
    while i>0:
        s+=x[i-1]
        i-=1
    while j>0:
        s+=y[j-1]
        j-=1
    return s[::-1]
x="acbcf"
y="abcdaf"
print("Shortest Common Subsequence is ",printScs(x,y))