# Problem: Third Maximum Number
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

import heapq
class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        heap = [-x for x in nums]
        heapq.heapify(heap)
        if len(heap) < 3:
            return -heap[0]
        heapq.heappop(heap)
        heapq.heappop(heap)
        return -heapq.heappop(heap)
