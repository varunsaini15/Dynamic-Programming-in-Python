import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------------------
'''
prob: climbing stairs optimized space

1. Objective function:
    f(i) is no. of distinct ways to reach the top
2. Identify base cases
    f(0)=1
    f(1)=1
3. Recurrence relation
    f(n)=f(n-1)+f(n-2)
4. Order of computation
    Bottom-up
5. Answer will be in f(n)

'''
#Time complexity: O(n)
#Space complexity: O(1)

def climbStairs(n):
    a,b=1,1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    
    return c
print(climbStairs(5))

'''
prob: climbing stairs 3 steps
1. Objective function:
    f(i) is no. of distinct ways to reach the top
2. Identify base cases
    f(0)=1
    f(1)=1
    f(2)=2
3. Recurrence relation
    f(n)=f(n-1)+f(n-2)
4. Order of computation
    Bottom-up
5. Answer will be in f(n)
'''
print("--------------------------")
def climbStairs_3(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

    return dp[n]
print(climbStairs_3(8))

'''
prob: climbing stairs k steps
1. Objective function:
    f(i) is no. of distinct ways to reach the top
2. Identify base cases
    f(0)=1
    f(1)=1
3. Recurrence relation
    f(n)=f(n-1)+f(n-2)+......f(n-k)
4. Order of computation
    Bottom-up
5. Answer will be in f(n)
'''
print("--------------------------")
def climbStairsk(n,k):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1#not needed
    for i in range(2,n+1):
        for j in range(1,k+1):
            # if i-j < 0:
            #     continue
            try:
                dp[i]+=dp[i-j]
            except:
                pass
    return dp[n]
print(climbStairsk(5,2))
print(climbStairsk(5,3))
print(climbStairsk(8,3))