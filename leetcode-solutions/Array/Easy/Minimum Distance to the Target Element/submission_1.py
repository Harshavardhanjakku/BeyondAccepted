# Problem: Minimum Distance to the Target Element
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def getMinDistance(self, nums, target, start):
        n = len(nums)
        left = right = start
        while left >= 0:
            if nums[left] == target:
                break
            left -= 1

        while right < n:
            if nums[right] == target:
                break
            right += 1 
        if left < 0:
            return abs(right - start)
        if right >= n:
            return abs(start - left) 
        return min(abs(start - left), abs(right - start))
