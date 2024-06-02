class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag2=n&1
        n=n>>1
        while(n):
            flag1=n&1
            if(flag1==flag2):
                return False
            flag2=flag1
            n=n>>1
        return True