class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo={}
        def dp(ind,prev_ind):
            if ind==len(nums):
                return 0
            key=(ind,prev_ind)
            if key in memo:
                return memo[key]
            len1=dp(ind+1,prev_ind)
            if(prev_ind==-1 or nums[ind]>nums[prev_ind]):
                len1=max(len1,1+dp(ind+1,ind))
            memo[key]=len1
            return len1
        return dp(0,-1)
            

            
