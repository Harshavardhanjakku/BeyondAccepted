# Problem: Angle Between Hands of a Clock
# Difficulty: Medium
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        deg=minutes*6 
        tothours=hour%12
        part=minutes*0.5 
        totdegree=(tothours)*30+part
        a=abs(deg-totdegree)
        return min(a,abs(360-a))
