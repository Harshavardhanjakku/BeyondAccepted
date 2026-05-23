# Count Pairs Of Similar Strings
# Difficulty: Easy
# Language: python

class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n=len(words)
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    count+=1
        return count
