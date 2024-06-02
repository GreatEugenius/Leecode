class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        空间复杂度优化 n**2->n+1
        """
        m,n=len(word1),len(word2)
        dp= [i for i in range(0,m+1)]
        for i in range(0,n):
            temp=dp[0]
            dp[0]=i+1
            for j in range(0,m):
                temp2=dp[j+1]
                if(word1[j]==word2[i]):
                    dp[j+1]=temp
                else:
                    dp[j+1] =min(dp[j],temp,dp[j+1])+1
                temp=temp2
        return dp[m]

    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n=len(word1),len(word2)
        dp=[[i for i in range(0,m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=i
        for i in range(0,n):
            for j in range(0,m):
                if(word1[j]==word2[i]):
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i+1][j+1] =min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
        return dp[n][m]


word1 = "horse"
word2 = "ros"
test=Solution()
print(test.minDistance(word1, word2))
