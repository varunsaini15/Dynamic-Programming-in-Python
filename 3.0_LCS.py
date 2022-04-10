import sys
from functools import lru_cache
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Longest common subseuqence(Recursive)----------
@lru_cache(None)
def lcs(x,y,m,n):
    if n==0 or m==0:
        return 0
    if x[m-1]==y[n-1]:
        return 1+lcs(x,y,m-1,n-1)
    else:
        return max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))
x="ylqpejqbalahwrfgj"
y="yrkzavgdmdgtqpggfj"
m=len(x)
n=len(y)
print("Lenght of lcs is : ",lcs(x,y,m,n))


# [Done] exited with code=0 in 48.282 seconds (without lru_cache)
# [Done] exited with code=0 in 0.15 seconds (with lru_cache)
