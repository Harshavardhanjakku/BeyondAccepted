# Problem: Count the Number of Special Characters I
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        dic={}
        for i in word :
            dic[i]=dic.get(i,0)+1
        count=0
        for i in dic :
            if i.islower() and i.upper() in dic :
                count+=1
        return count
