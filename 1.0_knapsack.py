import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#--------------------------------
'''
Input:
1 3 4 5
1 4 5 7
7
Output: 9
'''
def knapsack(wt,val,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    elif wt[n-1]>W:
        return knapsack(wt,val,W,n-1)
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
W=int(input())
n=len(wt)

print("Maximum Profit is =",knapsack(wt,val,W,n))
