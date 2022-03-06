from cmath import cos
import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#--------------------------
#RECONSTRUCt THE SOLUTION
#THE STEPS TAKEN TO MINIMIZE SOMETHING.
#OR THE PATH TAKEN TO REACH A MAX/MIN SOLUTION

'''
TAKING PROBLEM:
Paid staircase problem
object: return the cheapest path to reach top
'''
def paidStaircase2(n,p):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=p[1]
    arr=[]
    for i in range(2,n+1):
        dp[i]=p[i]+min(dp[i-1],dp[i-2])
        if dp[i-1]<dp[i-2]:
            arr.append(i-1)
        else:
            arr.append(i-2)
    path=[]
    arr.append(i)
    print(arr)
    # i=n-1
    # while i>0:
    #     path.append(i)
    #     i=arr[i]
'''dont know what to do'''

#     print(path)
        

#     return dp[n]
# p=[0,3,2,4,6,1,1,5,3]
# print(paidStaircase2(8,p))