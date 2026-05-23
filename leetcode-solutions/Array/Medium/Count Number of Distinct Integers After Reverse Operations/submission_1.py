# Problem: Count Number of Distinct Integers After Reverse Operations
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.extend([int(str(x)[::-1]) for x in nums])
        return len(set(nums))
