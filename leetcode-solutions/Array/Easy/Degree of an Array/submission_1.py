# Problem: Degree of an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findShortestSubArray(self, nums):
        freq = {}
        first = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            freq[num] = freq.get(num, 0) + 1
        degree = max(freq.values())
        ans = len(nums)

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if freq[num] == degree:
                ans = min(ans, i - first[num] + 1)
                freq[num] = 0      
        return ans
