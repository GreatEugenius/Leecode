class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return nums[0]
        pre0 = 0
        pre1 = 0
        for i in range(len(nums)-1):
            if (pre0 + nums[i]) > pre1:
                temp = pre0 + nums[i]
                pre0 = pre1
                pre1 = temp
            else:
                pre0 = pre1
        ans=pre1
        pre0 = 0
        pre1 = 0
        for i in range(len(nums)-1):
            if (pre0 + nums[i+1]) > pre1:
                temp = pre0 + nums[i+1]
                pre0 = pre1
                pre1 = temp
            else:
                pre0 = pre1
        print(pre1)
        return max(ans,pre1)

nums = [1,2,3,1]
test=Solution()
print(test.rob(nums))