# Problem: Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 4

from heapq import heappush, heappop, heapify

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = nums[:k]
        heapify(minheap)
        for num in nums[k:]:
            if num > minheap[0]:  
                heappop(minheap)  
                heappush(minheap, num)

        return minheap[0]

