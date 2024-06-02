import math


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        for i in range(2,n+1):
            for j in range(i//2,0,-1):
                if(i%j==0):
                    if(j==1):
                        dp[i]=i
                    else:
                        dp[i]=dp[j]+dp[i//j]
                    break
        return dp[n]


n=6
test=Solution()
print(test.minSteps(n))