# Uncommon Words from Two Sentences
# Difficulty: Easy
# Language: python

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        l=[]
        fs=s1.split()
        ss=s2.split()
        for i in fs:
            if fs.count(i)==1 and i not in ss:
                l.append(i)
        for i in ss:
            if ss.count(i)==1 and i not in fs:
                l.append(i)
        return l
        


        
