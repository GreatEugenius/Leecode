class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m,n=len(matrix),len(matrix[0])
        max_matix=[[0]*n for _ in range(m)]
        max=0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]=="1"):
                    max_matix[i][j]=1
                    if(i>0 and j>0):
                        max_matix[i][j]=min(max_matix[i-1][j],max_matix[i][j-1],max_matix[i-1][j-1])+1
                    if(max_matix[i][j]>max):
                        max=max_matix[i][j]
        return max*max


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
test=Solution()
print(test.maximalSquare(matrix))