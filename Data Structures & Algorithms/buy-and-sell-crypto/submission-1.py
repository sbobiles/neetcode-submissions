class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        brute solution
        Time complexity: O(n^2)
        '''

        bestProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if(prices[j] - prices[i] > bestProfit):
                    bestProfit = prices[j] - prices[i]
                
        return bestProfit