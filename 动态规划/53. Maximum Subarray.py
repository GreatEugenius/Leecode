class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        dp[0]=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if(dp[i-1]<0):
                dp[i]=nums[i]
            else:
                dp[i]= dp[i-1]+nums[i]
            ans=max(ans,dp[i])
        return ans
test=Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(test.maxSubArray(nums))