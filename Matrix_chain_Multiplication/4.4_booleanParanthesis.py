import sys
import math
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------Boolean Paranthesis----------------
def solve(s,i,j,isTrue):
    if i>j:
        return 0
    if i==j:
        return 1 if s[i]==isTrue else 0

    if isTrue=='T':
        x=0
    else:
        x=1
    
    if dp[i][j][x]!=-1:
        return dp[i][j][x]
    ans=0
    for k in range(i+1,j,2):
        lt=solve(s,i,k-1,"T")
        rt=solve(s,k+1,j,"T")
        lf=solve(s,i,k-1,"F")
        rf=solve(s,k+1,j,"F")

        if s[k]== "&":
            if isTrue=="T":
                ans+=lt*rt 
            else:
                ans+=lt*rf + rt*lf + lf*rf 
        elif s[k]=='|':
            if isTrue=='T':
                ans+=lt*rt + lt*rf + rt*lf 
            else:
                ans+=lf*rf 
        elif s[k]=='^':
            if isTrue=='T':
                ans+=lt*rf+rt*lf 
            else:
                ans+=lt*rt +lf*rf 
    dp[i][j][x]=ans 
    return ans 

s="T|T&F^T"
n=len(s)
dp = [[[-1]*2 for _ in range(n+1)] for _ in range(n+1)]
print(solve(s,0,n-1,"T"))