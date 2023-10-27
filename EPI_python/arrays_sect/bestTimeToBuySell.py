
"""
You are given an integer array prices where prices[i] 
is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

E

B
P
I
V




"""

def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0
        
        # high(ignore) -> low(buy)
        # low(buy) -> high(sell)
        profit = 0
        i = 0
        j = 1
        
        while j < len(prices):
            if prices[i] > prices[j]:
                i += 1
                j += 1
            elif prices[i] < prices[j]:
                profit = profit + prices[j] - prices[i]
                i += 1
                j += 1
            elif prices[i] == prices[j]:
                i += 1
                j += 1
            
        return profit