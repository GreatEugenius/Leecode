class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*(n+1) for _ in range(m+1)]
        for word in strs:
            num0=word.count("0")
            num1=len(word)-num0
            for i in range(m,num0-1,-1):
                for j in range(n, num1 - 1, -1):
                    dp[i][j]=max(dp[i][j],dp[i-num0][j-num1]+1)
        return dp[m][n]



strs = ["10","0001","111001","1","0"]
m = 5
n = 3
test=Solution()
print(test.findMaxForm(strs, m, n))