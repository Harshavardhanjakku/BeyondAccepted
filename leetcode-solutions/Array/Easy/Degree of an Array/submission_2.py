# Problem: Degree of an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        maxfreq = max(freq.values())
        ans = len(nums)
        for num in freq:
            if freq[num] == maxfreq:
                first = nums.index(num)
                last = len(nums) - 1 - nums[::-1].index(num)
                ans = min(ans, last - first + 1)
        return ans
        
