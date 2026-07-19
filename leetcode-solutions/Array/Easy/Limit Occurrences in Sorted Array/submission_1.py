# Problem: Limit Occurrences in Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] <= k:
                res.append(num)
        return res
