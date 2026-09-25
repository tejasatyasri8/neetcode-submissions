class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=len(matrix[0])-1
        r=0
        while(r<len(matrix) and c>=0):
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r+=1
            elif matrix[r][c]>target:
                c-=1
        return False
