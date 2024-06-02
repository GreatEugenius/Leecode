class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0 for i in range(len(nums))]
        for i in range(1,len(nums)-1):
            if(nums[i]-nums[i-1])==(nums[i+1]-nums[i]):
                dp[i]=dp[i-1]+1
        return sum(dp)


nums = [1,2,3,4]
test=Solution()
print(test.numberOfArithmeticSlices(nums))