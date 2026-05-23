# Problem: Richest Customer Wealth
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

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
