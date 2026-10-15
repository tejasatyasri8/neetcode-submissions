class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m=len(grid)
        self.n=len(grid[0])
        self.count=0
        def dfs(i,j):
            if(i<0 or i>=self.m or j<0 or j>=self.n or grid[i][j]=="0"):
                return False
            grid[i][j]="0"
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]=="1":
                    self.count+=1
                    dfs(i,j)
        return self.count