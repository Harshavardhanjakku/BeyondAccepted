# Problem: Furthest Point From Origin
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        lc=moves.count("L")
        rc=moves.count("R")
        uc=moves.count("_")
        return max(lc,rc)-min(lc,rc)+uc
