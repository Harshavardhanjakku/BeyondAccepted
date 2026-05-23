# Problem: Find Smallest Letter Greater Than Target
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in letters:
            if ord(i)>ord(target):
                return i
        return letters[0]
