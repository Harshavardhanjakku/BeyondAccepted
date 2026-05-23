# Problem: Find the Highest Altitude
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        point=0
        maxi=point
        for i in gain:
            point+=i
            if point>maxi:
                maxi=point
        return maxi
        
