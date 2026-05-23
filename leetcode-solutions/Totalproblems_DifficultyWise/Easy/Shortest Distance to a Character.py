# Shortest Distance to a Character
# Difficulty: Easy
# Language: python

class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        res = []

        for idx in range(n): 
            left = idx
            while left >= 0 and s[left] != c:
                left -= 1 
            right = idx
            while right < n and s[right] != c:
                right += 1 
            if left >= 0 and right < n:
                res.append(min(idx - left, right - idx))
            elif left >= 0:
                res.append(idx - left)
            else:
                res.append(right - idx)

        return res

