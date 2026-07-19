# Problem: Count Digit Appearances
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        tot = 0
        d = str(digit)

        for num in nums:
            tot += str(num).count(d)

        return tot
