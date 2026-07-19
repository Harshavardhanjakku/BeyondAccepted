# Problem: Hamming Distance
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 3

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0 
        while x or y :
            if x&1 != y&1:
                count+=1
            x>>=1
            y>>=1
        return count
