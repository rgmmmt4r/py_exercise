class Solution:
    def maxProfit(self, prices: list[int]) -> int: 
        lowest = prices[0]
        profit = 0
        for idx in range(len(prices)):
            if lowest > prices[idx]:
                lowest = prices[idx]
            if prices[idx] - lowest > profit:
                profit = prices[idx] - lowest
        return profit
