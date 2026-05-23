# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mymin=prices[0]
        profit=0
        for i in prices[1:]:
            if i<mymin:
                mymin=i
            profit=max(profit,i-mymin)
        return profit
            
