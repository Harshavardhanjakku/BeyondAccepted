# Problem: Decode XORed Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr=[first]
        for i in encoded:
            arr.append(i^arr[-1])
        return arr

