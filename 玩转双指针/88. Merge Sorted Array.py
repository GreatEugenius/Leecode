class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m+j]=nums2[j]
        nums1.sort()
        print(nums1)

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=m+n-1
        while(i>=0 and j>=0):
            if(nums1[i]<nums2[j]):
                nums1[k]=nums2[j]
                k-=1
                j-=1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        if(j>=0):
            for i in range(j+1):
                nums1[i] = nums2[i]
        print(nums1)




test=Solution()


nums1 = [0]
m = 0
nums2 = [1]
n = 1
test.merge2(nums1, m, nums2, n)