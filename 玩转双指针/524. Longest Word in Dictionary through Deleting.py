class Solution(object):
    def findWord(self, s, word):
        i=0
        j=0
        while(j<len(word)):
            if(i>=len(s)):
                return False
            if(s[i]==word[j]):
                i+=1
                j+=1
            else:
                i+=1
        return True

    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort(key=lambda x:(-len(x), x))
        for i in dictionary:
            if(self.findWord(s,i)):
                return i
        return ""





s = "abpcplea"
dictionary = ["b","a","c"]

test=Solution()
print(test.findLongestWord(s,dictionary))