class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin=0
        end=len(nums)-1
        min=nums[0]
        while(begin<=end):
            mid=int((begin+end)/2)
            if(nums[begin]==nums[mid]):
                if (min > nums[begin]):
                    min = nums[begin]
                begin+=1
            elif(nums[begin]<nums[mid]):
                if(min>nums[begin]):
                    min=nums[begin]
                begin=mid+1
            else:
                if (min > nums[mid]):
                    min = nums[mid]
                end=mid-1
        return min

test=Solution()
nums = [3,1]
print(test.findMin(nums))