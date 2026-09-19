class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxp=0
        # buy=0
        # sell=1
        # while(sell<len(prices)):
        #     if(prices[sell]<prices[buy]):
        #         buy=sell
        #     else:
        #         profit=prices[sell]-prices[buy]
        #         maxp=max(profit,maxp)
        #     sell+=1            
        # return maxp
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit