# Problem: Jump Game
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 5

class Solution(object):
    def canJump(self, a):
        n = len(a)
        if n == 1:
            return True
        if a[0] == 0:
            return False
        curr = a[0]
        for i in range(1, n):
            curr -= 1
            if curr < 0:
                return False
            curr = max(curr, a[i])
        return True

