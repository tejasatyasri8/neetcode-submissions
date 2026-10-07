import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict1=[]
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            distance=((x)**2+(y)**2)**(1/2)
            dict1.append([distance,x,y])
        heapq.heapify(dict1)
        res=[]
        while k>0:
            distance,x,y=heapq.heappop(dict1)
            res.append([x,y])
            k-=1
        return res
        