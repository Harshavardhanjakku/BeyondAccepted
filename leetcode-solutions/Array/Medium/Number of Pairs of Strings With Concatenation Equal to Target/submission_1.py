# Problem: Number of Pairs of Strings With Concatenation Equal to Target
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(n):
                if nums[i]+nums[j]==target and i!=j:
                    count+=1
        return count
