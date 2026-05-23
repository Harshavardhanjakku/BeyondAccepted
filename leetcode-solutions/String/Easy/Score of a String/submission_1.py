# Problem: Score of a String
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)-1):
            sum+=abs(ord(s[i])-ord(s[i+1]))
        return sum
            
        
