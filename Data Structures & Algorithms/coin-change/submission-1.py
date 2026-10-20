class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cal={}
        
        def dp(amount):
            if amount==0:
                return 0
            if amount in cal:
                return cal[amount]
            mincoins = float('inf')
            
            for i in range(len(coins)):
                if(coins[i]<=amount):
                    rem=amount-coins[i]
                    coin=1+dp(rem)
                    mincoins=min(mincoins,coin)
            cal[amount]=mincoins
            return mincoins
        ans=dp(amount)
        return ans if ans!=float('inf') else -1