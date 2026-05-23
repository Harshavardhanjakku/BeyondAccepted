# Problem: Maximum Number of Words Found in Sentences
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max([len(x.split()) for x in sentences])
