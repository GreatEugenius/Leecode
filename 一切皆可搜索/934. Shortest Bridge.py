class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        direction=[-1,0,1,0,-1]
        zero_point=[]
        def dfs(i,j):
            if(i>=0 and i<m and j>=0 and j<n):
                if(grid[i][j]==0):
                    zero_point.append([i,j])
                elif(grid[i][j]==1):
                    grid[i][j]=2
                    dfs(i+1,j)
                    dfs(i-1, j)
                    dfs(i, j+1)
                    dfs(i, j-1)
        flag=0
        for i in range(m):
            if(flag==0):
                for j in range(n):
                    if(grid[i][j]==1):
                        dfs(i,j)
                        flag=1
                        break
        level=0
        while(len(zero_point)>0):
            level+=1
            roundn=len(zero_point)
            while(roundn>0):
                x0,y0=zero_point.pop(0)
                roundn-=1
                for i in range(4):
                    x=x0+direction[i]
                    y=y0+direction[i+1]
                    if (x >= 0 and x < m and y >= 0 and y < n):
                        if(grid[x][y]==2):
                            continue
                        if(grid[x][y]==1):
                            return level
                        zero_point.append([x,y])
                        grid[x][y]=2
        return 0


grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
test=Solution()
print(test.shortestBridge(grid))