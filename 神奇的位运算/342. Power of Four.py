import math


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0:
            if 4** round(math.log(n,4),0)==n:
                return True
        return False

    def isPowerOfFour2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and not(n&(n-1)) and (n&1431655765)
n=16
test=Solution()
print(test.isPowerOfFour(n))