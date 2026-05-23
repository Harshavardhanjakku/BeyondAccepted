# First Matching Character From Both Ends
# Difficulty: Easy
# Language: python

class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        low=0
        high=n-1
        while low <=high:
            if s[low]==s[high]:
                return low
            low+=1
            high-=1
        return -1
