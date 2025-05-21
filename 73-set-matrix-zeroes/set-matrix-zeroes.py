class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def changerow(i):
            for j in range(n):
                if matrix[i][j]!=0:
                    matrix[i][j]=-2**31-1
        def changecol(j):
            for i in range(m):
                if matrix[i][j]!=0:
                    matrix[i][j]=-2**31-1
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    changerow(i)
                    changecol(j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-2**31-1:
                    matrix[i][j]=0

        