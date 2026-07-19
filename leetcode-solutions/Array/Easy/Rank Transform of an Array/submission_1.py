# Problem: Rank Transform of an Array
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {num: i for i, num in enumerate(sorted(set(arr)), 1)}
        return [rank[num] for num in arr]
