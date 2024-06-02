class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        flag=False
        for ch in s :
            if(ch=="i"):
                flag = not flag
            else:
                if(flag):
                    ans=ch+ans
                else:
                    ans=ans+ch
        if(flag):
            return  ans[::-1]
        else:
            return  ans


test=Solution()
s="string"
print(test.finalString(s))