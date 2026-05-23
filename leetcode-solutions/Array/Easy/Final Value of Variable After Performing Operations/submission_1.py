# Problem: Final Value of Variable After Performing Operations
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        p=operations.count("X++")+operations.count("++X")
        m=operations.count("X--")+operations.count("--X")
        return p-m
        
        
        
