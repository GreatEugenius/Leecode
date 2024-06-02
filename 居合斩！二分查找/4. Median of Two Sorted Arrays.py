class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums3=nums1+nums2
        nums3.sort()
        if (len(nums3)%2==0):
            i=int(len(nums3) / 2)
            return float(nums3[i]+nums3[i-1])/2
        else:
            return float(nums3[int((len(nums3))/2)])

nums1 = [1,2]
nums2 = [3,4]

test=Solution()
print(test.findMedianSortedArrays(nums1,nums2))
