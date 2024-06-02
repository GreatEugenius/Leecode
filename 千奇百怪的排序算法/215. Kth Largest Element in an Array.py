class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(key=lambda x:-x)
        return nums[k-1]

    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        k=r-k+1
        while(l<r):
            mid=self.quickSelection(nums,l,r)
            if(mid==k):
                return(nums[k])
            elif(mid<k):
                l=mid+1
            else:
                r=mid-1
        return nums[l]

    def quickSelection(self, nums, l,r):
        i=l+1
        j=r
        while(True):
            while(nums[i]<=nums[l] and i<r):
                i+=1
            while(nums[j]>=nums[l] and j>l):
                j-=1
            if(i>=j):
                break
            temp=nums[j]
            nums[j]=nums[i]
            nums[i]=temp
        temp = nums[j]
        nums[j] = nums[l]
        nums[l] = temp
        return j





nums = [3,3,3,3,3,3,3,3,3]
k = 1
test=Solution()
print(test.findKthLargest2(nums,k))