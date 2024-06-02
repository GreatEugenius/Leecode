class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        h = len(isConnected)
        def dfs(r):
            flag=0
            for i in range(h):
                if(isConnected[r][i]==1):
                    isConnected[r][i]=0
                    isConnected[i][r]=0
                    dfs(i)
                    flag=1
            return flag

        res=0
        for r in range(h):
            if(dfs(r)):
                res+=1
        return res

    def findCircleNum2(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        isVisit=[]
        num=0
        for i in range(len(isConnected)):
            isVisit.append(False)
        print(isVisit)
        def dfs(r):
            for j in range(len(isConnected)):
                if(not isVisit[j] and isConnected[r][j]==1):
                    isVisit[j]=True
                    dfs(j)
        for i in range(len(isConnected)):
            if(not isVisit[i]):
                isVisit[i] = True
                dfs(i)
                num+=1
        return  num




isConnected = [[1,1,0],[1,1,0],[0,0,1]]

test=Solution()
print(test.findCircleNum2(isConnected))

# for i in range(2,5):
#     print(i)