class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre0=0
        pre1=0
        for i in range(len(nums)):
            if (pre0+nums[i])>pre1:
                ans=pre0+nums[i]
                pre0=pre1
                pre1=ans
            else:
                pre0=pre1
        return pre1


nums = [1,2,3,1]
test=Solution()
print(test.rob(nums))