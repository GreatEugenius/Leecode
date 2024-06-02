class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=[]
        while True:
            m = 0
            while n != 0:
                r = n % 10
                m += r * r
                n = n // 10
            n=m
            if n==1:
                return True
            elif(n in seen):
                return False
            else:
                seen.append(n)
