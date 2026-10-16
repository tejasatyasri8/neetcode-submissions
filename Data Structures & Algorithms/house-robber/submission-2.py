class Solution:
    def rob(self, nums: List[int]) -> int:
        vis={}
        def dp(i):
            if(i in vis):
                return vis[i]
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            
            
            vis[i]=max(dp(i-1),nums[i]+dp(i-2))
            return vis[i]
        return dp(len(nums)-1)
