class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort(key=lambda x:-x)
        child = 0
        cookie = 0
        while (child < len(g) and cookie < len(s)):
            if (g[child] <= s[cookie]):
                child = child + 1
            cookie = cookie + 1

        return child

test=Solution()


g = [1,2,3]
s = [1,2]
# s.sort(key=lambda x:-x)
print(test.findContentChildren(g,s))

