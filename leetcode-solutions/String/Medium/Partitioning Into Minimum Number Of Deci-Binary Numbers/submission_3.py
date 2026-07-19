# Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
# Difficulty: Medium
# Topic: String
# Language: python3
# Submission: 3

class Solution:
    def minPartitions(self, n: str) -> int:
        res=0
        for i in n :
            res = max(res,int(i))
        return res

