class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        begin=0
        end=len(nums)-1
        while(begin<=end):
            mid=int((begin+end)/2)
            if(nums[mid]==target):
                return True
            if(nums[mid]==nums[end]):
                end-=1
            elif(nums[mid]<nums[end]):
                if(nums[mid]<target and nums[end]>=target):
                    begin=mid+1
                else:
                    end=mid-1
            else:
                if (nums[mid] > target and nums[begin] <=target):
                    end = mid - 1
                else:
                    begin=mid+1
        return False

test=Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(test.search(nums, target))