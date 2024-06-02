class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        dic = {}
        for char in t:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        count = 0
        start = 0
        min_length = len(s)+1
        min_start = 0
        for end in range(len(s)):
            if s[end] in dic:
                dic[s[end]] -= 1
                if dic[s[end]] >= 0:
                    count += 1
            while count == len(t):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    min_start = start
                if s[start] in dic:
                    dic[s[start]] += 1
                    if dic[s[start]] > 0:
                        count -= 1
                start += 1
        if min_length == (len(s)+1):
            return ""
        else:
            return s[min_start:min_start+min_length]

s = "ADOBECODEBANC"
t = "ABC"

test=Solution()
print(test.minWindow(s,t))