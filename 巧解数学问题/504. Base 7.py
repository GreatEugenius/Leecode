class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=""
        flag=False
        if(num<0):
            flag=True
            num=-num
        while(num!=0):
            low=num%7
            num=num//7
            ans=str(low)+ans
        if flag:
            return "-"+ans
        else:
            return ans

test=Solution()
num=-7
print(test.convertToBase7(num))
