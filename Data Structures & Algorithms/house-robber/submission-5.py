class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[-1]*(n+1)
        def dp(i):
            if(i==0):
                return nums[i]
            if(i<0):
                return 0
            if memo[i]!=-1:
                return memo[i]
            pick=nums[i]+dp(i-2)
            npick=dp(i-1)
            memo[i]=max(pick,npick)
            return memo[i]
        return dp(len(nums)-1)
            
