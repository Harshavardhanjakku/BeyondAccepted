# Problem: Sum of GCD of Formed Pairs
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        mx = 0
        arr = []
        for x in nums:
            mx = max(mx, x)
            arr.append(math.gcd(mx, x))
        arr.sort()
        ans = 0
        l, r = 0, len(arr) - 1
        while l < r:
            ans += math.gcd(arr[l], arr[r])
            l += 1
            r -= 1
        return ans
