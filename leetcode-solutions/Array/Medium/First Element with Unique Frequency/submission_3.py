# Problem: First Element with Unique Frequency
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        d1 = {}
        for i in nums:
            d1[i] = d1.get(i, 0) + 1
        d2 = {}
        for i in d1.values():
            d2[i] = d2.get(i, 0) + 1
        for i in nums:
            if d2[d1[i]] == 1:
                return i
        return -1
