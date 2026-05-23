# Problem:   Count Symmetric Integers
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 1

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        for i in range(low,high+1):
            n=len(str(i))
            if n%2==0 and sum(list(map(int,str(i)[:n//2])))==sum(list(map(int,str(i)[n//2::]))):
                count+=1
        return count


