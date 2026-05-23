# Problem: Number of Employees Who Met the Target
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        c=0
        for i in hours:
            if i>=target:
                c+=1
        return c
