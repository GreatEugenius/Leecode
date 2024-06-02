class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hash=[]
        ans=0
        for i in words:
            mask=0
            for j in i:
                mask=mask|1<<(ord(j)-97)
            length=len(i)
            for j in hash:
                if(j[0]&mask==0 and ans<j[1]*length):
                    ans=j[0]*length
            hash.append([mask,length])
        return ans

print(ord('c')-97)