# Problem: Angle Between Hands of a Clock
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 3

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        deg = minutes * 6
        part = minutes * 0.5 
        totdegree = (hour % 12) * 30 + part
        ans = abs(deg - totdegree)
        return min(ans, 360 - ans)
