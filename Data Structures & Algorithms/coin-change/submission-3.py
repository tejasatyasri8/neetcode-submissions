class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dp(idx,target):
            if(idx==0):
                if(target%coins[idx]==0):
                    return target//coins[idx]
                return float("inf")
            key=(idx,target)
            if(key in memo):
                return memo[key]
            ntake=0+dp(idx-1,target)
            take=float("inf")
            if(target>=coins[idx]):
               take= 1+dp(idx,target-coins[idx])
            memo[key]=min(ntake,take)
            return min(ntake,take)
        ans = dp(len(coins) - 1, amount)

        if ans == float("inf"):
            return -1
        return ans