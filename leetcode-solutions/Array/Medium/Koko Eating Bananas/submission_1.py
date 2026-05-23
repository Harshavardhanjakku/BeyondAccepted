# Problem: Koko Eating Bananas
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def minEatingSpeed(self, piles, h):
        def check(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            return total <= h
        low, high = 1, max(piles)
        while low <high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
