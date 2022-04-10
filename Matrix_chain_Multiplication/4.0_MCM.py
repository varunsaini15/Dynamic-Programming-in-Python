import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
from sys import stdin
input = stdin.readline
#---------Matrix Chain Multiplication-----------

'''
#------------ general format ------------
def solve(arr,i,j):
    if i>j :
        return 0
    for k in range(i,j):
        temp_ans=solve(arr,i,k) + solve(arr,k+1,j)
        ans = max(temp_ans)
    return ans
'''
def solve(arr,i,j):
    if i>=j:
        return 0
    ans=math.inf
    for k in range(i,(j-1)+1):
        cost=arr[i-1]*arr[k]*arr[j]
        temp_ans=solve(arr,i,k)+solve(arr,k+1,j)+cost 
        ans=min(ans,temp_ans)
    return ans 
arr=[40,20,30,10,30]
n=len(arr)
print("Minimum cost=",solve(arr,1,n-1))
















