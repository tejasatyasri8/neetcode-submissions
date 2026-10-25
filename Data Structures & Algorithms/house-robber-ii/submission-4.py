class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        # def helper(arr):
        #     n=len(arr)
        #     memo=[-1]*n
        #     def dp(i):
        #         if(i==0):
        #             return arr[0]
        #         if(i<0):
        #             return 0
        #         if(memo[i]!=-1):
        #             return memo[i]
        #         take=arr[i]+dp(i-2)
        #         ntake=dp(i-1)
        #         memo[i]=max(take,ntake)
        #         return memo[i]
        #     return dp(n-1)
        # ans1=helper(nums[:n-1])
        # ans2=helper(nums[1:])
        # return max(ans1,ans2)
        def helper(nums1):
            memo=[-1]*len(nums1)
            memo[0]=nums1[0]
            for i in range(1,len(nums1)):
                take=nums1[i]
                if(i>1):
                    take+=memo[i-2]
                ntake=memo[i-1]
                memo[i]=max(take,ntake)
            return memo[-1]
        ans1=helper(nums[1:])
        ans2=helper(nums[:-1])
        return max(ans1,ans2)
    
            