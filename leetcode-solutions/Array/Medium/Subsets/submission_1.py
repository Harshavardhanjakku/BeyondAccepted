# Problem: Subsets
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        subsets=[]
        for i in range(1<<n):
            subs=[]
            for j in range(n):
                if (i>>j)&1:
                    subs.append(nums[j])
            subsets.append(subs)
        return subsets
