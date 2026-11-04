class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        res=[]
        i=1
        newinterval=intervals[0]
        # while(i<len(intervals)):
        #     j=i
        #     while(j<len(intervals) and intervals[j][0]<=newinterval[1]):
        #         newinterval[0]=min(newinterval[0],intervals[j][0])
        #         newinterval[1]=max(newinterval[1],intervals[j][1])
        #         j+=1
        #     res.append(newinterval)
        #     i=j
        #     if i < len(intervals):
        #         newinterval = intervals[i]
        # if newinterval not in res:
        #     res.append(newinterval)
        
        # return res
        while(i<len(intervals)):
            if(intervals[i][0]<=newinterval[1]):
                newinterval[0]=min(newinterval[0],intervals[i][0])
                newinterval[1]=max(newinterval[1],intervals[i][1])
            else:
                
                res.append(newinterval)
                newinterval=intervals[i]
            i+=1
            
        res.append(newinterval)
        return res                
        

