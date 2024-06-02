class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans=[0 for i in range(len(temperatures))]
        stack=[]
        for i in range(len(temperatures)):
            while(len(stack)!=0):
                pre=stack[len(stack)-1]
                if(temperatures[i]<=temperatures[pre]):
                    break
                ans[pre]=i-pre
                stack.pop()
            stack.append(i)
        return ans


temperatures = [73,74,75,71,69,72,76,73]
test=Solution()
print(test.dailyTemperatures(temperatures))