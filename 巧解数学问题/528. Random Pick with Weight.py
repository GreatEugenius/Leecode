import random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.total = sum(w)
        self.list = [0 for _ in range(len(w))]
        for i in range(len(w)):
            if i == 0:
                self.list[i] = w[i]
            else:
                self.list[i] = w[i] + self.list[i - 1]
    def pickIndex(self):
        """
        :rtype: int
        """
        rand=random.randint(0,self.total-1)
        for i in range(len(self.list)):
            if(rand<self.list[i]):
                return i

# Your Solution object will be instantiated and called as such:
w=[1,3]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)