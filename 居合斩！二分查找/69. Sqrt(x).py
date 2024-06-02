class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x==0):
            return 0
        begin=1
        end=x
        while((begin+1)<end):
            mid = int((begin + end) / 2)
            if(mid*mid>x):
                end=mid
            elif(mid*mid<x):
                begin=mid
            else:
                return mid
        return begin






test=Solution()


x = 6
print(test.mySqrt(x))