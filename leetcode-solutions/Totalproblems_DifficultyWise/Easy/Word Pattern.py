# Word Pattern
# Difficulty: Easy
# Language: python

class Solution(object):
    def wordPattern(self, pattern, s):
        d = {}
        d2 = {}
        low = s.split()

        if len(pattern) != len(low):
            return False

        for idx, val in enumerate(pattern): 
            if val not in d:
                d[val] = low[idx]
            elif d[val] != low[idx]:
                return False
 
            if low[idx] not in d2:
                d2[low[idx]] = val
            elif d2[low[idx]] != val:
                return False

        return True

