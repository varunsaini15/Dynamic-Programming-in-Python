import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Min no of ins.. del.. to convert string x to string y-----------        
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
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

def printMinDelAndInsert(str1,str2):
    m=len(str1)
    n=len(str2)
    leng=lcs(str1,str2)
    print("Minimum number of insertions = ",n - leng)
    print("Minimum number of deletions = ",m - leng)

str1 = "heap"
str2 = "pea"
printMinDelAndInsert(str1, str2)