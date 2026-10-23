class Solution:
    def climbStairs(self, n: int) -> int:
        # memo=[-1]*(n+1)
        # def dp(i):
        #     if i==0 or i==1:
        #         return 1
        #     if memo[i]!=-1:
        #         return memo[i]
        #     memo[i]=dp(i-1)+dp(i-2)
        #     return memo[i]
        # return dp(n)

        # dp=[-1]*(n+1)
        prev=1
        prev1=1
        for i in range(2,n+1):
            x=(prev+prev1)
            prev=prev1
            prev1=x
            
        return prev1