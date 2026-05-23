# Problem: Height Checker
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected=sorted(heights)
        n=len(expected)
        c=0
        for i in range(n):
            if heights[i]!=expected[i]:
                c+=1
        return c
