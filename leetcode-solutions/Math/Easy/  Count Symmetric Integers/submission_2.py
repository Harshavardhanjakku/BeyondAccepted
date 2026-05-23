# Problem:   Count Symmetric Integers
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        for i in range(low,high+1):
            temp=str(i)
            n=len(temp)
            mid=n//2
            if n%2==0:
                if sum(list(map(int,temp[:mid])))==sum(list(map(int,temp[mid::]))):
                    count+=1
        return count


