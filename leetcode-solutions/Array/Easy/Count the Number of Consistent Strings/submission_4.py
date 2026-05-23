# Problem: Count the Number of Consistent Strings
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for i in words:
            if all([x in allowed for x in i]):
                count+=1
        return count

