class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=prices[0]
        ans=0
        for i in range(1,len(prices)):
            dp=min(prices[i],dp)
            ans=max(ans,prices[i]-dp)
        return ans



prices = [7,1,5,3,6,4]
test=Solution()
print(test.maxProfit(prices))