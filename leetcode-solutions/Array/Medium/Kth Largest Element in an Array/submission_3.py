# Problem: Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        return  heapq.nlargest(k,nums)[-1]

