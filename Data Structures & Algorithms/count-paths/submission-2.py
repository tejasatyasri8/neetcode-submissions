class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        demo=[[-1]*n for _ in range(m)]
        def dfs(i,j):
            if(i==0 and j==0):
                return 1
            if(i<0 or j<0):
                return 0
            if(demo[i][j]!=-1):
                return demo[i][j]
            up=dfs(i-1,j)
            left=dfs(i,j-1)
            demo[i][j]=up+left
            return demo[i][j]
        return dfs(m-1,n-1)

        demo=[[-1]*n for _ in range(m)]
        demo[0][0]=1
        for i in range(m):
            for j in range(n):
                if(i==0 and j==0):
                    continue
                else:
                    up=0
                    left=0
                    if(i>0):
                        up=demp[i-1][j]
                    if(j>0):
                        left=demo[i][j-1]
                    demo[i][j]=up+left
        print(demo[m-1][n-1])
