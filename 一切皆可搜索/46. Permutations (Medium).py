class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)

        def backtracking(num,level):
            if(level==(n-1)):
                ans.append(num.copy())
                return
            else:
                for i in range(level,n):
                    num[i],num[level]=num[level],num[i]
                    backtracking(num,level+1)
                    num[i], num[level] = num[level], num[i]

        backtracking(nums,0)
        return ans

nums = [0,1,2]
test=Solution()
print(test.permute(nums))