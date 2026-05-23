# Problem: Find Most Frequent Vowel and Consonant
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def maxFreqSum(self, s):
        vowels = set("aeiou")
        freq = {}
        vmax = 0
        cmax = 0
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            if ch in vowels:
                vmax = max(vmax, freq[ch])
            else:
                cmax = max(cmax, freq[ch])
        return vmax + cmax
