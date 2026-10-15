class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        visited=set()
        def dfs(i,j,ocean,visited):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
                return False    
            if(ocean=="Atlantic" and (i==len(heights)-1 or j==len(heights[0])-1) ):
                return True
            if(ocean=="Pacific" and (i==0 or j==0 )):
                return True
            if((i,j) in visited):
                return False
            visited.add((i,j))

            for ni,nj in([i+1,j],[i-1,j],[i,j+1],[i,j-1]):
                if(0<=ni<len(heights) and 0<=nj<len(heights[0])):
                    if(heights[ni][nj]<=heights[i][j]):
                        if dfs(ni,nj,ocean,visited):
                            return True
            return False
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                Pacific=dfs(i,j,"Pacific",set())
                Atlantic=dfs(i,j,"Atlantic",set())
                if(Pacific and Atlantic):
                    res.append([i,j])
        return res