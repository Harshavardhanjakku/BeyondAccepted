# Problem: Sorting the Sentence
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        mylist=s.split()
        d={}
        for i in mylist:
            d[int(i[-1])]=i[:-1]
        k=''
        for i in range(1,len(mylist)+1):
            k=k+d[i]+' '
        return k[:-1]
        
        
