class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def help(i):
            if i in memo:
                return memo[i]
            if(i==1):
                return 1
            if(i==2):
                return 2
            memo[i]=help(i-1)+help(i-2)
            return memo[i]
        if(n>=1):
            return help(n)
        return 0