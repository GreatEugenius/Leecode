class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid);
        w = len(grid[0]);
        area = 0;

        def dfs(g, r, c):
            if 0 <= r < h and 0 <= c < w and g[r][c] == 1:
                g[r][c] = '#'
                return 1 + dfs(g, r - 1, c) + dfs(g, r, c + 1) + dfs(g, r + 1, c) + dfs(g, r, c - 1)
            else:
                return 0

        for r in range(h):
            for c in range(w):
                if grid[r][c] == 1:  area = max(area, dfs(grid, r, c))

        return area

    # hope it helps

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
test=Solution()
print(test.maxAreaOfIsland(grid))