# Problem: Count of Matches in Tournament
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        total = 0
        advance = 0
        while n>1 :
            if n%2:
                matches=(n - 1)// 2
                advance=(n - 1)//2 + 1
            else:
                matches=n//2
                advance=n//2
            total += matches
            print(n,matches,advance)
            n=advance
        return total






