class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        dp=[-1]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                if(dp[i-coin]!=-1):
                    if(dp[i]!=-1):
                        dp[i]=min(dp[i],dp[i-coin]+1)
                    else:
                        dp[i] = dp[i - coin] + 1
        return dp[amount]

coins = [2]
amount = 3
test=Solution()
test.coinChange(coins,amount)
