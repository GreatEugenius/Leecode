class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        pp = []
        for i in dic:
            pp.append([i, dic[i]])

        pp.sort(key=lambda x: (-x[1],x[0]))
        res = ""
        for i in pp:
            for j in range(i[1]):
                res+=i[0]
        return res

s = "tree"
test=Solution()
print(test.frequencySort(s))