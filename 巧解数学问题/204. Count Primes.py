import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<3):
            return 0
        count=(n-2)//2+1
        prime=[True]*(n+1)
        sqrtn=int(math.sqrt(n))+1
        for i in range(3,sqrtn,2):
            for j in range(3*i,n,i*2):
                if(prime[j]):
                    prime[j]=False
                    count-=1
        return count

test=Solution()
n=10
print(test.countPrimes(n))