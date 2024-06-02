class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]
        for i in range(1,len(nums)):
            ans=ans^nums[i]
        return ans

nums = [2,2,1,1,3]
test=Solution()
print(test.singleNumber(nums))