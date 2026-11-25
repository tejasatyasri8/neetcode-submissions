class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ds=[]
        def ss(idx,ds):
            if(idx==len(nums)):
                res.append(sorted(ds.copy()))
                return
            #pick
            ds.append(nums[idx])
            ss(idx+1,ds)
            ds.pop()
            #not pick
            ss(idx+1,ds)
        ss(0,ds)
        set1=set()
        for i in range(len(res)):
            set1.add(tuple(res[i]))

        return [list(x) for x in set1]
        
            
