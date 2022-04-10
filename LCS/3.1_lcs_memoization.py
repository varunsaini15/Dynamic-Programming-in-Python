import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Longest common subseuqence(Memoization/Top Down)----------

def lcs(x,y,m,n):
    if m==0 or n==0:
        return 0
    if dp[m][n]!= -1:
        return dp[m][n]
    if x[m-1]==y[n-1]:
        dp[m][n] = 1+lcs(x,y,m-1,n-1)
        return 1+lcs(x,y,m-1,n-1)
    else:
        dp[m][n] = max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
        return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
    
dp=[[-1]*1001 for i in range(1001)]    
def main():
    x="ylqpejqbalahwrfgj"
    y="yrkzavgdmdgtqpggfj"
    m=len(x)
    n=len(y)
    print("length of lcs =",lcs(x,y,m,n))
main()