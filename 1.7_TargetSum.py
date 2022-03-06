'''
Solution of count no. of subsets with given difference:
---------------------------------------------------------
def Countsubsetsum(arr,Sum,n):
    dp=[[0]*(Sum+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for j in range(1,Sum+1):
        dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,Sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]             
    return dp[n][Sum]
----------------------------------------------------------
arr= [1,1,2,3]
diff=1
# OP: 3
n=len(arr)
Sum=(diff+sum(arr))//2 #New code 
print(Countsubsetsum(arr,Sum,n))
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
             TARGET SUM PROBLEM (leetcode):

1)This problem is same as count the number of subsets with given difference.
2)The only change is that the sum is (target+sum(arr))/2
-----------------------------------------------------------
'''
class Solution:
    def findTargetSumWays(self, nums, target):
        if abs(target)>sum(nums): 
            return 0       
        if (target+sum(nums))%2!=0:
            return 0
        n=len(nums)
        Sum=(target+sum(nums))//2

        dp=[[0]*(Sum+1) for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1
        for j in range(1,Sum+1):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(Sum+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]
