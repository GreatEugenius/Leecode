class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(len(s)+1):
            for j in range(i):
                if(dp[j]==True and s[j:i] in wordDict):
                    dp[i]=True
        return dp[len(s)]


test=Solution()

s = "catsanddog"
wordDict = ["cats","dog","sand","and","cat"]
print(test.wordBreak(s,wordDict))