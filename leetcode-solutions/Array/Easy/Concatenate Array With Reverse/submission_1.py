# Problem: Concatenate Array With Reverse
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums) 
        for i in range(n-1,-1,-1):
            nums.append(nums[i])
        return nums
