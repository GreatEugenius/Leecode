class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans=0
        for i in range(32):
            ans=(ans<<1)|(n&1)
            n=n>>1
        return ans





n = 43261596
test=Solution()
print(test.reverseBits(n))