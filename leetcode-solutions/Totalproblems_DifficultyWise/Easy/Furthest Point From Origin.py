# Furthest Point From Origin
# Difficulty: Easy
# Language: python

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        lc = rc = uc = 0
        for ch in moves:
            if ch == 'L':
                lc += 1
            elif ch == 'R':
                rc += 1
            else:
                uc += 1
        return abs(lc - rc) + uc
