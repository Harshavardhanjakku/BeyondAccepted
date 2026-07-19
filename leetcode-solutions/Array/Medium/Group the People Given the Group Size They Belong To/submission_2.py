# Problem: Group the People Given the Group Size They Belong To
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i in range(len(groupSizes)):
            dic[i] = groupSizes[i]
        arr = sorted(dic.items(), key=lambda x: x[1])
        res = []
        i = 0
        while i < len(arr):
            size = arr[i][1]
            group = []
            for j in range(size):
                group.append(arr[i + j][0])
            res.append(group)
            i += size

        return res
