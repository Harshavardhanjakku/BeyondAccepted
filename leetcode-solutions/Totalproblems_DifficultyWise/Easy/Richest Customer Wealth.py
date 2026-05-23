# Richest Customer Wealth
# Difficulty: Easy
# Language: python

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max=0
        for i in accounts:
            tot=sum(i)
            if tot>max:
                max=tot
        return max
