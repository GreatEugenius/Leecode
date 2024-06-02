import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        numsp=self.nums[:]
        for i in range(len(numsp)):
            temp=numsp[i]
            j=random.randint(0,len(numsp)-1)
            numsp[i]=numsp[j]
            numsp[j]=temp
        return numsp



# Your Solution object will be instantiated and called as such:
nums=[1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)