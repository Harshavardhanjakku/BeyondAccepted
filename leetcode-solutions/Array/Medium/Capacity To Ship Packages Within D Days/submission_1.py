# Problem: Capacity To Ship Packages Within D Days
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def shipWithinDays(self, weights, days):
        return self.binarysearch(weights, days)

    def check(self, weights, days, capacity):
        countdays = 1
        wc = 0
        for w in weights:
            if wc + w <= capacity:
                wc += w
            else:
                countdays += 1
                wc = w
        return countdays <= days

    def binarysearch(self, weights, days):
        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if self.check(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

