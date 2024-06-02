import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=0
        j=int(math.sqrt(c))
        while(i<=j):
            temp=i*i+j*j
            if(temp==c):
                return True
            elif(temp>c):
                j-=1
            else:
                i+=1
        return False

test=Solution()
c = 4
print(test.judgeSquareSum(c))