# Problem: Sort Characters By Frequency
# Difficulty: Medium
# Topic: Hash Table
# Language: python3
# Submission: 1

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        res = ""
        for key, value in sorted(dic.items(), key=lambda x: x[1], reverse=True):
            res += key * value
        return res
