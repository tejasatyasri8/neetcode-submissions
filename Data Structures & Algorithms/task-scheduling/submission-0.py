class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count={}
        for ele in tasks:
            task_count[ele]=task_count.get(ele,0)+1
        cycles=[-val for val in task_count.values()]
        max_heap = cycles.copy()
        heapq.heapify(max_heap)
        queue=deque()
        time=0
        while queue or max_heap:
            time+=1
            if queue and queue[0][1]==time:
                task=queue.popleft()
                heapq.heappush(max_heap,task[0])
            if max_heap:
                x=heapq.heappop(max_heap)
                x+=1
                if(x<0):
                    queue.append([x,time+n+1])
        return time
