class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=1
        freetime=intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]>=freetime):
                count+=1
                freetime=intervals[i][1]

        return len(intervals)-count