# Redistribute Characters to Make All Strings Equal
# Difficulty: Easy
# Language: python

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        fw="".join(words)
        n=len(words)
        l=[fw.count(i) for i in set(fw)]
        if all([x%n==0 for x in l]):
            return True
        else:
            return False
