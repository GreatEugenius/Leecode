class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp=[0]*(n+1)
        for i in range(1,n+1):
            if(i%2==0):
                dp[i]=dp[i>>1]
            else:
                dp[i]=dp[i-1]+1
        return dp

n=5
test=Solution()
print(test.countBits(n))