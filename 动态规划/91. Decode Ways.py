class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[1]*(n+1)
        if(s[0]=="0"):
            return 0
        for i in range(1,n):
            if(int(s[i])==0):
                if(int(s[i-1])>0 and  int(s[i-1])<3):
                    dp[i+1]=dp[i-1]
                else:
                    return 0
            elif (int(s[i])<=6 and int(s[i-1])==2) or (int(s[i-1])==1) :
                dp[i + 1] = dp[i-1]+dp[i]
            else:
                dp[i + 1] = dp[i]
        print(dp)
        return dp[n]

if __name__=="__main__":
    s = "2611055971756562"
    test=Solution()
    print(test.numDecodings(s))
