import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Sequence pattern matching-----------
def lcs(x,y):
    m,n=len(x),len(y)
    t=[[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[-1][-1]

x='axy'
y='adxcpy'
if len(x)==lcs(x,y):
    print("Yes")
else:
    print('No')
#------------------Simple 2 pointer----------------------
# a='axy'
# b='adxcpy'
# m,n=len(a),len(b)
# i,j=0,0
# while i!=m or j!=n:
#     if a[i]==b[j]:
#         i+=1
#         j+=1
#     else:
#         j+=1
# if i==m:
#     print("Yes")
# else:
#     print("No")