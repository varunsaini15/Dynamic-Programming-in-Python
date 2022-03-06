import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#----------------------------
'''
Modified space complexity for k steps.
'''
def climbStairsk(n,k):
    dp=[0]*(k)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(1,k):
            # if i-j < 0:
            #     continue
            try:
                dp[i%k]+=dp[(i-j)%k]
            except:
                pass
    return dp[n%k]


print(climbStairsk(5,3))

'''
Problem:
Not allowed to step on 'red' stair.
Problem:
	Climbing Stairs (k steps, space optimized, skip red steps)
	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can climb 1..k steps. You are not allowed to step on red stairs.
	In how many distinct ways can you climb to the top?
'''

# Time complexity: O(nk)
# Space complexity: O(k)
stairs=[False, True, False, True, True, False, False]
def climbStairsk_red(n,k,stairs):
    dp=[0]*(k)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(1,k):

            if stairs[i-1]:
                dp[i%k]=0
            else:
                try:
                    dp[i%k]+=dp[(i-j)%k]
                except:
                    pass
    print(dp)
    return dp[n%k]

print(climbStairsk_red(7,3,stairs))
