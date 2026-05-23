# Problem: Convert the Temperature
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius+273.15,celsius*1.80+32.00]
        
