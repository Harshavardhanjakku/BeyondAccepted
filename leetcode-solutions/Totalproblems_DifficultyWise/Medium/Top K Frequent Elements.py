# Top K Frequent Elements
# Difficulty: Medium
# Language: python

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        freq = sorted(freq.items(), key=lambda x: -x[1])
        return [key for key, _ in freq[:k]]
