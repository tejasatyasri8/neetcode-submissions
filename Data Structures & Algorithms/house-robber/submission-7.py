class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[-1]*(n)
        # def dp(i):
        #     if(i==0):
        #         return nums[i]
        #     if(i<0):
        #         return 0
        #     if memo[i]!=-1:
        #         return memo[i]
        #     pick=nums[i]+dp(i-2)
        #     npick=dp(i-1)
        #     memo[i]=max(pick,npick)
        #     return memo[i]
        # return dp(len(nums)-1)
        # memo[0]=nums[0]
        # for i in range(1,n):
        #     take=nums[i]
        #     if i>1:
        #         take+=memo[i-2]
        #     ntake=memo[i-1]
        #     memo[i]=max(take,ntake)
        # return memo[-1]
        memo[0]=nums[0]
        prev1=memo[0]
        prev2=0
        for i in range(1,n):
            take=nums[i]
            if(i>1):
                take+=prev2
            ntake=prev1
            curr=max(take,ntake)
            prev2=prev1
            prev1=curr
            memo[i]=curr
        return prev1

        
        

    
            
