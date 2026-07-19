# Problem: Rank Transform of an Array
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mylist = sorted(set(arr))
        dic = {}

        for rank, value in enumerate(mylist, start=1):
            dic[value] = rank

        return [dic[x] for x in arr]
