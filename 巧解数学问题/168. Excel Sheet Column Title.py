class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans=""
        while columnNumber>0:
            if(columnNumber%26==0):
                ans = "Z" + ans
                columnNumber=columnNumber-26
            else:
                ans=chr(columnNumber%26+64)+ans
            columnNumber=columnNumber//26

        return ans

test=Solution()
print(test.convertToTitle(1))