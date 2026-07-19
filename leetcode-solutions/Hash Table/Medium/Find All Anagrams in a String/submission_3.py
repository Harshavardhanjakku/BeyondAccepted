# Problem: Find All Anagrams in a String
# Difficulty: Medium
# Topic: Hash Table
# Language: python
# Submission: 3

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        k = len(p)
        if k > n:
            return []
        pdic = {}
        for ch in p:
            pdic[ch] = pdic.get(ch, 0) + 1
        wdic = {}
        for ch in s[:k]:
            wdic[ch] = wdic.get(ch, 0) + 1
        res = []
        if wdic == pdic:
            res.append(0)
        for i in range(k, n):
            left = s[i - k]
            wdic[left] -= 1
            if wdic[left] == 0:
                del wdic[left]
            right = s[i]
            wdic[right] = wdic.get(right, 0) + 1
            if wdic == pdic:
                res.append(i - k + 1)
        return res
