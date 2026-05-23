# Problem: Plus One
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=list(map(str,digits))
        n=int("".join(s))
        n=n+1
        n=str(n)
        res=list(int(x) for x in n)
        return res
            
        
