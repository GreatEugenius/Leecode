class Solution:
    def combine(self, n, k):
        ans = []
        nums=[]

        def backtracking(nums, max):
            if (len(nums) == (k)):
                ans.append(nums.copy())
                return
            for i in range(max, n):
                if (i+1) not in nums:
                    nums.append(i+1)
                    backtracking(nums,i)
                    nums.pop()
        backtracking(nums, 0)
        return ans

    def combine2(self, n, k):
        ans=[]
        nums=[]
        def backtracking(nums, min):
            if(len(nums)==k):
                ans.append(nums.copy())
                return
            if(k-len(nums))<=(n-min):
                for i in range(min,n):
                    if (i+1) not in nums:
                        nums.append(i+1)
                        backtracking(nums, i)
                        nums.pop()
        backtracking(nums,0)
        return ans


test=Solution()
print(test.combine2(4,2))