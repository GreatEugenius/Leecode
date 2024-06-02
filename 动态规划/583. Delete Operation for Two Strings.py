class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word1)+1):
            dp[0][i]=i
        for i in range(len(word2)+1):
            dp[i][0]=i
        for i in range(len(word2)):
            for j in range(len(word1)):
                if(word1[j]==word2[i]):
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i+1][j],dp[i][j+1])+1
        return dp[len(word2)][len(word1)]

word1 = "sea"
word2 = "eat"
test=Solution()
print(test.minDistance(word1, word2))