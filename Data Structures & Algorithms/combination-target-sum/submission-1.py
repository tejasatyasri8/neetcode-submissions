class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        def cs(idx,target,curr):
            if(idx==len(nums)):
                if target==0:
                    res.append(curr.copy())
                return
            #pick
            if(nums[idx]<=target):
                curr.append(nums[idx])
                cs(idx,target-nums[idx],curr)
                curr.pop()
            cs(idx+1,target,curr)
        cs(0,target,curr)
        return res