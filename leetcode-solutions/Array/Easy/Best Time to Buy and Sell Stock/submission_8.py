# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mymin=float('inf')
        profit=float('-inf')
        for i in prices:
            mymin=min(mymin,i)
            profit=max(profit,i-mymin)
        return profit
            
