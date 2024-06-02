class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        flag=1
        flag2=1
        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            elif(flag==1):
                if(s[i]==s[j-1]):
                    if (flag2 > 0):
                        tem_i = i
                        tem_j = j
                        flag2 = 0
                    i+=1
                    j-=2
                    flag=0
                elif(s[i+1]==s[j]):
                    i+=2
                    j-=1
                    flag=0
                else:
                    return False
            else:
                if (flag2==0  and s[tem_i + 1] == s[tem_j]):
                    i = tem_i+2
                    j = tem_j-1
                    flag2=-1
                else:
                    return False
        return True

test=Solution()
s = "abc"
print(test.validPalindrome(s))