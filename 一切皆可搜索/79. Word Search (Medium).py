class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited=[[False for x in range(len(board[0]))] for y in range(len(board))]
        def backtracking(i,j,pos):
            if(i<0 or i>=len(board) or j<0 or j>=len(board[0])):
                return False
            if(visited[i][j] or board[i][j]!=word[pos]):
                return False
            if(pos==len(word)-1):
                return True
            visited[i][j] = True
            res=backtracking(i+1,j,pos + 1) or backtracking(i-1, j, pos + 1) or backtracking(i, j+1, pos + 1) or backtracking(i, j-1, pos + 1)
            visited[i][j]=False
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (backtracking(i,j,0)):
                    return True
        return False

test=Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(test.exist(board, word))