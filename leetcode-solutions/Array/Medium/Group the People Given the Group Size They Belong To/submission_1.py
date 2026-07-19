# Problem: Group the People Given the Group Size They Belong To
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        res = []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
        return res
