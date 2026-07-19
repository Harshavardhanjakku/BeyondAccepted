# Problem: Sum of GCD of Formed Pairs
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 5

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        n = len(nums)
        prefix = [0] * n
        curr = 0
        for i in range(n):
            curr = max(curr, nums[i])
            prefix[i] = math.gcd(curr, nums[i])
        prefix.sort()
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            ans += math.gcd(prefix[left], prefix[right])
            left += 1
            right -= 1
        return ans
