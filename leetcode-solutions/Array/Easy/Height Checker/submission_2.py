# Problem: Height Checker
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        el=sorted(heights)
        n=len(el)
        count=0
        for i,j in zip(heights,el):
            if i!=j:
                count+=1
        return count
