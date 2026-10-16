class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for i in range(n)]
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        visited=[0 for i in range(n)]
        count=0
        def dfs(node):
            if(visited[node]==1):
                return
            visited[node]=1
            for neighbor in graph[node]:
                dfs(neighbor)
        for i in range(len(visited)):
            if(visited[i]==0):
                count+=1
                dfs(i)
        return count