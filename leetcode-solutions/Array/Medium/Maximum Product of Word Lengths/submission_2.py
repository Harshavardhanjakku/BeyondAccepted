# Problem: Maximum Product of Word Lengths
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        masks = [0] * n
        lens = [0] * n 
        for i, w in enumerate(words):
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask
            lens[i] = len(w)

        maxi = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:   
                    maxi = max(maxi, lens[i] * lens[j])

        return maxi

