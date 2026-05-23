# Final Value of Variable After Performing Operations
# Difficulty: Easy
# Language: python

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        p=operations.count("X++")+operations.count("++X")
        m=operations.count("X--")+operations.count("--X")
        return p-m
        
        
        
