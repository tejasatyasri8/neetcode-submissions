class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=[[] for _ in range(n)]
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        state=[0 for i in range(n)]
        def dfs(node,parent):
            state[node]=1
            for neighbour in graph[node]:
                if(state[neighbour]==1 and neighbour!=parent):
                    return False
                if(state[neighbour]==0):
                    if not dfs(neighbour,node):
                        return False
            return True
        if not dfs(0,-1):
            return False
        for i in state:
            if i==0:
                return False
        return True