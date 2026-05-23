# Problem: Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 6

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        heapify(h)
        for i in nums:
            heappush(h, -i)
        for i in range(k-1):
            heappop(h)
        return -h[0]
