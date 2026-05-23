# Problem: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s==target:
                return [i+1,j+1]
            elif s<target:
                i+=1
            else:
                j-=1
        
