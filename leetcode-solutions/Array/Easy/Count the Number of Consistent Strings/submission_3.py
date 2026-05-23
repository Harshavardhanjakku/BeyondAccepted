# Problem: Count the Number of Consistent Strings
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        s=set(allowed)
        for i in words:
            if all([x in s for x in set(i)]):
                count+=1
        return count

