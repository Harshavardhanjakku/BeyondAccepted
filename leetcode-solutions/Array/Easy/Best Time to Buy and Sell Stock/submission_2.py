# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > max_profit:
                max_profit = price - min_value 
        return max_profit
      







