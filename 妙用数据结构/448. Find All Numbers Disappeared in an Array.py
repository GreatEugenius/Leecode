class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        flag=[0 for i in range(len(nums))]
        for i in nums:
            flag[i-1]=1
        for i in range(len(flag)):
            if(flag[i]==0):
                ans.append(i+1)
        return ans