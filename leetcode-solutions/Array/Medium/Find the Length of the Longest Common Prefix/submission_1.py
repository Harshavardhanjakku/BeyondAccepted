# Problem: Find the Length of the Longest Common Prefix
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()
        for num in arr1:
            s = str(num)
            temp = ""
            for ch in s:
                temp += ch
                prefixes.add(temp)
        res = 0 
        for num in arr2:
            s = str(num)
            temp = ""
            for ch in s:
                temp += ch
                if temp in prefixes:
                    res = max(res, len(temp))
        return res
