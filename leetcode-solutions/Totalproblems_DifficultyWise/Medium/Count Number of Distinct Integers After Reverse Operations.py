# Count Number of Distinct Integers After Reverse Operations
# Difficulty: Medium
# Language: python

class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.extend([int(str(x)[::-1]) for x in nums])
        return len(set(nums))
