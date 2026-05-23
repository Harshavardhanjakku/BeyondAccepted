# Problem: Permutations
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
 
        return list(permutations(nums))
