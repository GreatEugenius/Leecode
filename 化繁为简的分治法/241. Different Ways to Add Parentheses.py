class Solution(object):

    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if(expression.isdigit()):
            return [int(expression)]
        index=[]
        ans=[]
        for i in range(len(expression)):
            if not expression[i].isdigit():
                index.append(i)
        for i in range(len(index)):
            a=self.diffWaysToCompute(expression[0:index[i]])
            b=self.diffWaysToCompute(expression[index[i]+1:len(expression)+1])
            if(expression[index[i]]=="+"):
                for j in a:
                    for k in b:
                        ans.append(j+k)
            elif (expression[index[i]] == "-"):
                for j in a:
                    for k in b:
                        ans.append(j-k)
            elif (expression[index[i]] == "*"):
                for j in a:
                    for k in b:
                        ans.append(j*k)
            elif (expression[index[i]] == "/"):
                for j in a:
                    for k in b:
                        ans.append(j/k)
        return ans

expression = "2*3-4*5"
test=Solution()
print(test.diffWaysToCompute(expression))