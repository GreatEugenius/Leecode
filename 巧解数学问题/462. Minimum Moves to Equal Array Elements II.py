class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_median(data):
            sorted_data = sorted(data)
            n = len(sorted_data)
            mid = n // 2

            # 对于奇数长度的列表，返回中间的元素
            if n % 2 == 1:
                return sorted_data[mid]
            # 对于偶数长度的列表，返回中间两个元素的平均值
            else:
                return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        target = find_median(nums)
        ans =0
        for i in nums:
            ans= ans + abs(i-target)
        return ans