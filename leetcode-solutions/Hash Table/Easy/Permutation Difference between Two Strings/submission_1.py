# Problem: Permutation Difference between Two Strings
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res=0
        ind=0
        for i in s:
            res+=abs(ind-t.index(i))
            ind+=1
        return res

        
