# Problem: First Missing Positive
# Difficulty: Hard
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        c=0
        for i in nums:
            if i>0:
                s.add(i)
            c+=1
        for i in range(1,c+2):
            if i not in s:
                return i
            
        
