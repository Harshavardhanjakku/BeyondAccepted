# Problem: Maximum Number of Balloons
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 3

class Solution(object):
    def maxNumberOfBalloons(self, text):
        dic = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for ch in text:
            if ch in dic:
                dic[ch] += 1
        return min(dic["b"],dic["a"],dic["l"] // 2,dic["o"] // 2,dic["n"])
