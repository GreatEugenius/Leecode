class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        ans =nums[0]
        for i in nums[1:]:
            if(count==0):
                ans = i
                count = 1
            elif(ans==i):
                count =count +1
            else:
                count = count - 1
        return ans