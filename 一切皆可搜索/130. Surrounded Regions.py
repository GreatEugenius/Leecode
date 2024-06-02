class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        def dfs(i,j):
            if i< 0 or j < 0 or i >= m or j >= n or board[i][j] == "X" or board[i][j] =="Y":
                return
            board[i][j]="Y"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if(board[i][j]=="O" and (i==0 or i ==m-1 or j==0 or j==n-1)):
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if(board[i][j]=="Y"):
                    board[i][j]="O"
                elif (board[i][j] == "O"):
                    board[i][j] = "X"



board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
for i in board:
    print(i)
text=Solution()
text.solve(board)
for i in board:
    print(i)