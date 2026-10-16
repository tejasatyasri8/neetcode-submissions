class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        state=[0 for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        def dfs(course):
            if(state[course]==1):
                return False
            if(state[course]==2):
                return True
            state[course]=1
            for i in range(len(graph[course])):
                if not dfs(graph[course][i]):
                    return False
            state[course]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True