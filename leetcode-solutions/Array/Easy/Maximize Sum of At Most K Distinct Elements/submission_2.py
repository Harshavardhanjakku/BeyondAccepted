# Problem: Maximize Sum of At Most K Distinct Elements
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        l=list(set(nums))
        l.sort(reverse=True)
        print(l)
        return l[:k]


        
