class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        rain=[]
        for i in range(len(height)):
            if(height[i]>max):
                max=height[i]
            rain.append(max-height[i])
        max=0
        for i in range(len(height)-1,-1,-1):
            if (height[i] > max):
                max = height[i]
            rain[i]=min(max-height[i],rain[i])
        return sum(rain)







height = [4,2,0,3,2,5]
test=Solution()
print(test.trap(height))