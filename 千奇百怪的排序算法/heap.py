class Heap(object):
    def __init__(self,nums):
        self.nums=nums
    def heapify(self,nums,n,i):
        large=i
        left=i*2+1
        right=i*2+2
        if(left<n and nums[left]>nums[large]):
            large=left
        if (right < n and nums[right] > nums[large]):
            large = right
        if(large!=i):
            nums[i],nums[large]=nums[large],nums[i]
            self.heapify(nums,n,large)

    def buildHeap(self):
        n=len(nums)
        for i in range(((n-2)//2),-1,-1):
            self.heapify(nums,n,i)

    def sortHeap(self):
        n=len(nums)
        for i in range(n-1,0,-1):
            nums[i],nums[0]=nums[0],nums[i]
            self.heapify(nums,n=i,i=0)

    def topNHeap(self,m):
        m-=1
        n = len(nums) - 1
        while(m):
            nums[n],nums[0]=nums[0],nums[n]
            self.heapify(nums,n=n,i=0)
            m-=1
            n-=1
        return nums[0]

nums=[1,3,4,6,8,5]
test=Heap(nums)
test.buildHeap()
# test.sortHeap()
print(test.topNHeap(2))