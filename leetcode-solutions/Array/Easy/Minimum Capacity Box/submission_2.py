# Problem: Minimum Capacity Box
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n=len(capacity)
        index=-1
        curr=float('inf')
        for i in range(n):
            if capacity[i]>=itemSize and capacity[i]<curr:
                index=i
                curr=capacity[i]
        return index 
