# Problem: Top K Frequent Words
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def topKFrequent(self, words, k):
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        arr = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, freq in arr[:k]]
