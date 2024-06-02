import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        mimSquare=list(range(0,n+1))
        for i in range(n+1):
            j=1
            while(j*j<=i):
                mimSquare[i]=min(mimSquare[i],mimSquare[i-j*j]+1)
                j+=1
        return mimSquare[n]

n = 13
test=Solution()
print(test.numSquares(n))