class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        pp=[]
        for i in dic:
            pp.append([i,dic[i]])

        pp.sort(key=lambda x:-x[1])
        res = []
        for i in range(k):
            res.append(pp[i][0])
        return res


nums = [1,1,1,2,2,3]
k = 2
test=Solution()
print(test.topKFrequent(nums,k))