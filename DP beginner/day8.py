import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#-----------------------
'''
Problem:
	Paint Fence With Two Colors
	There is a fence with n posts, each post can be painted with either green or blue color.
	You have to paint all the posts such that no more than two adjacent fence posts have the same color.
	Return the total number of ways you can paint the fence.
'''

def numWays(n):
    dp=[[0]*2 for i in range(n+1)]
    dp[1][0]=1
    dp[1][1]=1
    dp[2][0]=2 #10, 00
    dp[2][1]=2 #01, 11
    for i in range(3,n+1):
        for j in range(2):
            dp[i][j]=dp[i-1][1-j]+dp[i-2][1-j]
    return dp[n][0]+dp[n][1]