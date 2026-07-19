# Problem: Weighted Word Mapping
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []
        for word in words:
            totw = 0
            for ch in word:
                totw += weights[ord(ch) - 97]
            rem = totw % 26
            ans.append(chr(ord('z') - rem))
        return "".join(ans)
