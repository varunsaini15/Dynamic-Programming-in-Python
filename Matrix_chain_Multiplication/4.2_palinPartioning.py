import math
import sys
input = sys.stdin.buffer.readline
from functools import lru_cache
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#---------Palindrome partioning recursive-----------
def ispalin(t):
    if t==t[::-1]:
        return True
    return False 

@lru_cache(None)
def solve(s,i,j):   
    if i>=j:
        return 0
    if ispalin(s[i:j+1]):
        return 0
    ans=math.inf
    for k in range(i,(j-1)+1,1):
        if ispalin(s[i:k+1]):
            tmp_ans=solve(s,i,k)+solve(s,k+1,j)+1
        ans=min(ans,tmp_ans)
    return ans
s="aab"
print("Ans is ",solve(s,0,len(s)-1))