# Problem: Maximize Sum of At Most K Distinct Elements
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), reverse=True)[:k]
