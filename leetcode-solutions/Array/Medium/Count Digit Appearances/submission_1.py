# Problem: Count Digit Appearances
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return str(nums).count(str(digit))
