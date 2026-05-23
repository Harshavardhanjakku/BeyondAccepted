# Problem: Longest Common Prefix
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 4

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        import string
        checkstring=strs[0]
        maxi=""
        for j in range(len(checkstring)):
            if all([x.startswith(checkstring[:j+1]) for x in strs]):
                maxi=checkstring[:j+1]
        return maxi
