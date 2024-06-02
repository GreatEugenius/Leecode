class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        mul=1
        for i in range(len(nums)-2,-1,-1):
            mul=mul*nums[i+1]
            ans[i]=ans[i]*mul
        return ans

test=Solution()

nums = [1,2,3,4]
print(test.productExceptSelf(nums))