class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n=len(mat),len(mat[0])
        ans=[[max(m,n)]*n for i in range(m)]
        if (mat[0][0] == 0):
            ans[0][0] = 0
        for i in range(1,m):
            if(mat[i][0]==0):
                ans[i][0]=0
            else:
                ans[i][0]=ans[i-1][0]+1
        for i in range(1,n):
            if(mat[0][i]==0):
                ans[0][i]=0
            else:
                ans[0][i]=ans[0][i-1]+1
        for i in range(1,m):
            for j in range(1,n):
                if(mat[i][j]==0):
                    ans[i][j]=0
                else:
                    ans[i][j]=min(ans[i-1][j],ans[i][j-1])+1
        print(ans)
        for i in range(m-2,-1,-1):
            if(mat[i][n-1]==0):
                ans[i][n-1]=0
            else:
                ans[i][n-1]=min(ans[i+1][n-1]+1,ans[i][n-1])
        for i in range(n-2,-1,-1):
            if(mat[m-1][i]==0):
                ans[m-1][i]=0
            else:
                ans[m-1][i]=min(ans[m-1][i+1]+1,ans[m-1][i])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if(mat[i][j]==0):
                    continue
                else:
                    ans[i][j]=min(ans[i+1][j]+1,ans[i][j+1]+1,ans[i][j])
        return ans

    def updateMatrix2(self, mat):
        m,n=len(mat),len(mat[0])
        bfsQueue=[]
        direction=[-1,0,1,0,-1]
        visited=[[False] * n for i in range(m)]
        ans=[[m] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    visited[i][j]=True
                    ans[i][j]=0
                    bfsQueue.append((i,j))
        while bfsQueue:
            p,q=bfsQueue.pop(0)
            dis=ans[p][q]
            for k in range(4):
                i=p+direction[k]
                j = q + direction[k+1]
                if(i>=0 and i<m and j>=0 and j<n and not visited[i][j]):
                    ans[i][j] = dis+1
                    visited[i][j]=True
                    bfsQueue.append((i, j))
        return ans

mat =  [[0,0,0],[0,1,0],[1,1,1]]
test=Solution()
print(test.updateMatrix2(mat))