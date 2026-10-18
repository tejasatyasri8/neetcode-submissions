class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linear_rob(houses):
            vis={}
            def dp(i):
                if i in vis:
                    return vis[i]
                if(i==0):
                    return houses[0]
                if(i==1):
                    return max(houses[0], houses[1])
                vis[i]=max(dp(i-1),houses[i]+dp(i-2))
                return vis[i]
            return dp(len(houses)-1)
        return max(linear_rob(nums[1:]),linear_rob(nums[:-1]))