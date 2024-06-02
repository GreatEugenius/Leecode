class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if(k<1):
            return 0
        elif k>=len(prices)//2:
            ans=0
            for i in range(1,len(prices)):
                if prices[i-1]<prices[i]:
                    ans+=prices[i]-prices[i-1]
            return ans
        else:
            buy=[-max(prices)]*(k+1)
            sell=[0]*(k+1)
            for i in range(len(prices)):
                for j in range(1,k+1):
                    buy[j]=max(buy[j],sell[j-1]-prices[i])
                    sell[j]=max(sell[j],buy[j]+prices[i])
            return sell[k]
k = 1
prices = [1,2]
test=Solution()
print(test.maxProfit(k, prices))