class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin=0
        end=len(nums)-1
        while(begin<=end):
            mid=int((begin+end)/2)
            if(mid<len(nums)-1 and nums[mid]==nums[mid+1]):
                if(mid%2==1):
                    end=mid-1
                else:
                    begin=mid+1
            elif (mid!=0 and nums[mid] == nums[mid - 1]):
                if (mid % 2 == 0):
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                return nums[mid]
        return nums[begin]

nums = [1,1,2,3,3,4,4,8,8]
test=Solution()
print(test.singleNonDuplicate(nums))