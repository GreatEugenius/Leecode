class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=int(n/2)

        for i in range(m):
            for j in range(m+n%2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[n-j-1][i]
                matrix[n - j-1][i] = matrix[n - i-1][n - j-1]
                matrix[n - i-1][n - j-1] = matrix[j][n - i-1]
                matrix[j][n - i-1] =temp
        print(matrix)

test=Solution()
matrix =[[1,2,3],[4,5,6],[7,8,9]]
test.rotate(matrix)