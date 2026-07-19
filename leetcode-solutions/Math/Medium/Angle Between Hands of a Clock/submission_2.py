# Problem: Angle Between Hands of a Clock
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        a = (30*hour) - (5.5*minutes)
        return min(abs(a),abs(360-abs(a)))
        
