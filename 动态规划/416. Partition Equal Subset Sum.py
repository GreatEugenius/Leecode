class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        sum_nums=sum(nums)
        if(sum_nums%2):
            return False
        target=sum_nums//2
        dp=[[False]*(target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        for i in range(n):
            for j in range(1,target+1):
                if(j-nums[i]>=0):
                    dp[i][j]=dp[i-1][j]|dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n-1][target]

    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        sum_nums=sum(nums)
        if(sum_nums%2):
            return False
        target=sum_nums//2
        dp0=[False]*(target+1)
        dp0[0]=True
        for i in range(n):
            dp=dp0.copy()
            print(dp)
            for j in range(nums[i],target+1):
                dp[j]=dp0[j-nums[i]]
            for j in range(nums[i], target + 1):
                dp0[j]=dp0[j]|dp[j]
        return dp0[target]
nums = [1,2,5]
test=Solution()
print(test.canPartition2(nums))