# Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
# Difficulty: Medium
# Topic: String
# Language: python3
# Submission: 1

class Solution:
    def minPartitions(self, n: str) -> int:
        for i in range(9, -1, -1):
            if str(i) in n:
                return i
        

