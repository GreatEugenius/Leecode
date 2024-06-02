class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans=0
        n=1
        while(num>0):
            ans=ans+((num&1)^1)*n
            n=n*2
            num=num>>1
        return ans

num = 4
test=Solution()
print(test.findComplement(num))