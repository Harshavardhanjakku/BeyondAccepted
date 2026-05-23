# Problem: Minimum Capacity Box
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def minimumIndex(self,capacity:list[int],itemSize:int)->int:
        index=-1
        curr=float('inf')
        for i in range(len(capacity)):
            if capacity[i]>=itemSize and capacity[i]<curr:
                curr=capacity[i]
                index=i
        return index
