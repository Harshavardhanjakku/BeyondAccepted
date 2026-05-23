# Problem: Find Most Frequent Vowel and Consonant
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 2

class Solution(object):
    def maxFreqSum(self, s):
        from collections import Counter
        VOWELS = set("aeiou")
        freq = Counter(s)
        vmaxi = max([freq[c] for c in freq if c in VOWELS] or [0])
        cmaxi = max([freq[c] for c in freq if c not in VOWELS] or [0])

        return vmaxi + cmaxi
