class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin=0
        end=len(nums)
        while(begin<end):
            mid=int((begin+end)/2)
            if(nums[mid]>=target):
                end=mid
            else:
                begin=mid+1
        if(begin>len(nums) or nums[begin]!=target):
            return [-1,-1]
        res=begin
        begin = 0
        end = len(nums)
        while (begin < end):
            mid = int((begin + end) / 2)
            if (nums[mid] > target):
                end = mid
            else:
                begin = mid + 1
        return [res,begin-1]


test=Solution()

nums = [5,7,7,8,8,10]
target = 8
print(test.searchRange(nums, target))