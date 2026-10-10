class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        if(len(self.small)>(len(self.large)+1)):
            x=heapq.heappop(self.small)
            heapq.heappush(self.large,-x)
        elif(len(self.small)==(len(self.large)+1) and self.large):
            x=heapq.heappop(self.small)
            if -x>self.large[0]:
                y=heapq.heappop(self.large)
                heapq.heappush(self.large,-x)
                heapq.heappush(self.small,-y)
            else:
                heapq.heappush(self.small, x)


    def findMedian(self) -> float:
        med=0.0
        if(len(self.small)==len(self.large)):
            med=(-(self.small[0])+(self.large[0]))/2
        else:
            if(len(self.small)>len(self.large)):
                med=-(self.small[0])
            else:
                med=(self.large[0])
        return med