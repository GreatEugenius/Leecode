class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        min_path=[[grid[0][0]]*n for i in range(m)]
        for i in range(1,m):
            min_path[i][0]= min_path[i-1][0]+grid[i][0]
        for i in range(1,n):
            min_path[0][i]=min_path[0][i-1]+grid[0][i]

        for i in range(1,m):
            for j in range(1,n):
                min_path[i][j]=grid[i][j]+min(min_path[i-1][j],min_path[i][j-1])
        return min_path[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
test=Solution()
print(test.minPathSum(grid))