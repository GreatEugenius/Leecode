class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag=0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                if(i!=0 and nums[i-1]>nums[i+1]):
                    nums[i+1]=nums[i]
                flag+=1
                if (flag > 1):
                    return False
        return True





test=Solution()


nums = [4,2,3]
print(test.checkPossibility(nums))