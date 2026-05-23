# Decode XORed Array
# Difficulty: Easy
# Language: python

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res=[first]
        value=first
        for i in encoded:
            value=value^i
            res.append(value)
        return res
        
