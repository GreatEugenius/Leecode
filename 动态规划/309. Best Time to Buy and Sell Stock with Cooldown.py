class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=[0]*len(prices)
        sell = [0] * len(prices)
        s1= [0] * len(prices)
        s2 = [0] * len(prices)
        buy[0]=-prices[0]
        s1[0]=-prices[0]
        for i in range(1,len(prices)):
            buy[i]=s2[i-1]-prices[i]
            s1[i]=max(buy[i],s1[i-1])
            sell[i]=max(buy[i-1],s1[i-1])+prices[i]
            s2[i]=max(s2[i-1],sell[i-1])
        return max(s2[len(prices)-1],sell[len(prices)-1])


test=Solution()
prices = [1,2,3,0,2]
print(test.maxProfit(prices))
