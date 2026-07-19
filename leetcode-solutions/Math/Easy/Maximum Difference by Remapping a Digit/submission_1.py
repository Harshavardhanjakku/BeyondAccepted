# Problem: Maximum Difference by Remapping a Digit
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 1

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        i = 0
        while i < len(s):
            if s[i] != "9":
                break
            i+= 1
        if i < len(s):
            maxi=int(s.replace(s[i], "9"))
        else:
            maxi=num
        mini=int(s.replace(s[0], "0"))
        return maxi - mini
