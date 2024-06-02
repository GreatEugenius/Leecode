class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a)-1
        j=len(b)-1
        carry=0
        ans=""
        while(i>=0 or j>=0 or carry>0):
            if(i>=0):
                if(a[i]=='1'):
                    carry+=1
                i=i-1
            if (j >= 0):
                if (b[j] == '1'):
                    carry += 1
                j = j - 1
            ans=str(carry%2)+ans
            carry=carry//2
        return ans

test=Solution()
a="11"
b="1"
print(test.addBinary(a, b))