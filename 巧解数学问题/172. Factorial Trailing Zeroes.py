class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while(n!=0):
            n=n//5
            ans+=n
        return ans

test=Solution()
n=25
print(test.trailingZeroes(n))