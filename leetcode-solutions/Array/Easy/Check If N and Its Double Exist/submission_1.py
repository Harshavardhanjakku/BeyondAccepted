# Problem: Check If N and Its Double Exist
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s=set()
        for num in arr:
            if num*2 in s or (num%2==0 and num//2 in s):
                return True
            s.add(num)
        return False
