class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for i in nums:
            ans=ans^i
        for i in range(len(nums)):
            ans=ans^(i+1)
        return ans

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums) * (len(nums) + 1) / 2 - sum(nums)
        return ans