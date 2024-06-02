class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff=x^y
        ans=0
        while(diff>0):
            ans+=diff&1
            diff=diff>>1
        return ans


x = 1
y = 4
test=Solution()
print(test.hammingDistance(x, y))