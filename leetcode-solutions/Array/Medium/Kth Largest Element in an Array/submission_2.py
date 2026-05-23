# Problem: Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

