class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Pn=Pn-1+pn-2
        P=[1,2]
        for i in range(2,n):
            P.append(P[i-2]+P[i-1])
        return P[n-1]

test=Solution()
print(test.climbStairs(3))
