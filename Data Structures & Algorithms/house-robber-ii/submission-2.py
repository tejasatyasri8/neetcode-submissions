class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def helper(arr):
            n=len(arr)
            memo=[-1]*n
            def dp(i):
                if(i==0):
                    return arr[0]
                if(i<0):
                    return 0
                if(memo[i]!=-1):
                    return memo[i]
                take=arr[i]+dp(i-2)
                ntake=dp(i-1)
                memo[i]=max(take,ntake)
                return memo[i]
            return dp(n-1)
        ans1=helper(nums[:n-1])
        ans2=helper(nums[1:])
        return max(ans1,ans2)