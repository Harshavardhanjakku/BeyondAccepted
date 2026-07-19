# Problem: Count Digit Appearances
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return sum(str(num).count(str(digit)) for num in nums)
