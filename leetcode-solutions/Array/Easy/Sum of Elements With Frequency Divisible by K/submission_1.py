# Problem: Sum of Elements With Frequency Divisible by K
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sum(num * cnt for num, cnt in freq.items() if cnt % k == 0)
