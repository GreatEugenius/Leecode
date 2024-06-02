class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if(nums[i]>nums[j]):
                    ans[i]=max(ans[i],ans[j]+1)
        return max(ans)

nums = [7,7,7,7,7,7,7]
test=Solution()
print(test.lengthOfLIS(nums))