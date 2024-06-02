class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price=prices[0]
        profit=0
        for i in prices:
            if(i>price):
                profit=profit+i-price
            price=i
        return profit

test=Solution()


prices = [1,2,3,4,5]
print(test.maxProfit(prices))