class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # lis=[]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             lis.append([i,j])
        # for i in range(len(lis)):
        #     m,n=lis[i]
        #     for i in range(len(matrix)):
        #         matrix[i][n]=0
        #     for i in range(len(matrix[0])):
        #         matrix[m][i]=0

        lis1=[0 for _ in range(len(matrix))]
        lis2=[0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    lis1[i]=-1
                    lis2[j]=-1

        for i in range(len(lis1)):
            if lis1[i]==-1:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
        for i in range(len(lis2)):
            if lis2[i]==-1:
                for j in range(len(matrix)):
                    matrix[j][i]=0
