class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        buy=0
        sell=1
        while(sell<len(prices)):
            if(prices[sell]<prices[buy]):
                buy=sell
            else:
                profit=prices[sell]-prices[buy]
                maxp=max(profit,maxp)
            sell+=1            
        return maxp