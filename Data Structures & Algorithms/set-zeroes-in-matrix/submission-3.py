class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        lis=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    lis.append([i,j])
        for i in range(len(lis)):
            m,n=lis[i]
            for i in range(len(matrix)):
                matrix[i][n]=0
            for i in range(len(matrix[0])):
                matrix[m][i]=0