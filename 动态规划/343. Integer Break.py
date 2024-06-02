class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        for i in range(n):
            dp[i]=i
        for i in range(1,n+1):
            for j in range(0,i):
                dp[i]=max(dp[j]*dp[i-j],dp[i])

        return dp[n]


if __name__ == '__main__':
    test=Solution()
    n=10
    print(test.integerBreak(n))