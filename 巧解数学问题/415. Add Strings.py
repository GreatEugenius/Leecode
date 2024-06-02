class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans=""
        if(len(num2)>len(num1)):
            temp=num2
            num2=num1
            num1=temp
        len_1 = len(num1)
        len_2 = len(num2)
        add=0
        for i in range(len_1):
            if(i<len_2):
                ans=str((int(num1[len_1 - i - 1])+int(num2[len_2 - i - 1])+add)%10)+ans
                add=(int(num1[len_1 - i - 1])+int(num2[len_2 - i - 1])+add)//10
            else:
                ans = str((int(num1[len_1 - i - 1])+ add)% 10 ) + ans
                add = (int(num1[len_1 - i - 1])+ add)// 10
        if add!=0:
            ans=str(add)+ans
        return ans


num1 = "11"
num2 = "999"
test=Solution()
print(test.addStrings(num1,num2))