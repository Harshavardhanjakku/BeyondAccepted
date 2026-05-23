# Longest Common Prefix
# Difficulty: Easy
# Language: python3

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

