class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        ans=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if(text1[i-1]==text2[j-1]):
                    ans[i][j]=max(ans[i-1][j],ans[i][j-1],ans[i-1][j-1]+1)
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])
        return ans[len(text1)][len(text2)]


text1 = "abc"
text2 = "def"
test=Solution()
print(test.longestCommonSubsequence(text1, text2))