import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#-------------------------IMPORTANT QUESTIONS FOR INTERVIEW---------------------
'''
Problem:
	Unique Paths
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	How many possible unique paths are there?
	+---+---+---+---+
	| S |   |   |   |
	+---+---+---+---+
	|   |   |   |   |
	+---+---+---+---+
	|   |   |   | E |
	+---+---+---+---+
	Above is a 3 x 4 grid. How many possible unique paths are there?
'''
# f[i][j]=f[i-1][j]+f[i][j-1]
def uniquePaths(m,n):
    dp = [[0] * n for _ in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if i>0 and j>0:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            elif j>0:
                dp[i][j]=dp[i][j-1]
            elif i>0:
                dp[i][j]=dp[i-1][j]
            
    return dp[m-1][n-1]

# #or 
# dp = [[0] * n for _ in range(m)]        
#         for i in range(m):
#             for j in range(n):
#                 if i==0 and j==0:
#                     dp[i][j]=1
#                 elif i==0:
#                     dp[i][j]=dp[i][j-1]
#                 elif j==0:
#                     dp[i][j]=dp[i-1][j]
#                 else:
#                     dp[i][j]=dp[i-1][j]+dp[i][j-1]
#         return dp[m-1][n-1]

#----------------With obstacles----------
'''
Problem:
	Unique Paths with Obstales
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Now consider if some obstacles are added to the grids.
	How many unique paths would there be?
	+---+---+---+---+
	| S |   |   |   |
	+---+---+---+---+
	|   | 1 | 1 | 1 |
	+---+---+---+---+
	|   |   |   | E |
	+---+---+---+---+
	An obstacle and empty space is marked as 1 and 0 respectively in the grid.
'''

def uniquePathsObstacles(grid):
    m=len(grid)
    n=len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                dp[i][j]=0
                continue
            if i>0 and j>0:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            elif j>0:
                dp[i][j]=dp[i][j-1]
            elif i>0:
                dp[i][j]=dp[i-1][j]
            
    return dp[m-1][n-1]
#------------------Maximum profit in grid------------
#Optimisation problem
'''
Problem:
	Maximum Profit in a Grid
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	Each cell contains a coin the robot can collect.
	What is the maximum profit the robot can accumulate?
	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+'''
#d contains the coins we collect
# f[i][j]=max(f[i-1][j],f[i][j-1])+ d[i][j]
def maxProfit(grid):
    m=len(grid)
    n=len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if i>0 and j>0:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i][j]                
            elif j>0:
                dp[i][j]=dp[i][j-1] + grid[i][j]
            elif i>0:
                dp[i][j]=dp[i-1][j] + grid[i][j]
            
    return dp[m-1][n-1]