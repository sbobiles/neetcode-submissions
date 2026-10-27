class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        optimized
        Time complexity: O(n)
        '''
        bestProfit = 0

        #indices
        buy = 0
        sell = 1

        while (buy < sell) and (sell < len(prices)):
            if(prices[sell] - prices[buy] >= 0):
                bestProfit = max(prices[sell] - prices[buy], bestProfit)
                sell += 1
            else:
                buy = sell
                sell = buy + 1

        return bestProfit