# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mymin=99999999
        profit=0
        for i in prices:
            if i<mymin:
                mymin=i
            if i-mymin>profit:
                profit=i-mymin
        return profit
            
