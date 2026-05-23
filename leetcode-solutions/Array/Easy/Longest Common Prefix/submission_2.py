# Problem: Longest Common Prefix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smallest = min(strs, key=len)
        while smallest:
            if all(s.startswith(smallest) for s in strs):
                return smallest
            smallest = smallest[:-1]
        return ""

