# Problem: Special Array I
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n==1:
            return True
        for i in range(n-1):
            if (nums[i]+nums[i+1])%2==0:
                return False
        return True
