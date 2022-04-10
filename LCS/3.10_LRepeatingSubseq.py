import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Longest repeating subseuqence-----------
def lcs(x,y):
    m,n=len(x),len(y)
    t=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1]==y[j-1] and i!=j:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[-1][-1]

x="ABEBACDD"    
y=x[::]
print("LRS=",lcs(x,y))
