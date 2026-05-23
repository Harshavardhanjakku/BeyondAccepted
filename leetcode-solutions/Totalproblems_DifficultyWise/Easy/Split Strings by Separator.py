# Split Strings by Separator
# Difficulty: Easy
# Language: python

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        l=[i.split(separator) for i in words]
        return [ele for x in l for ele in x if ele!=""]
      
