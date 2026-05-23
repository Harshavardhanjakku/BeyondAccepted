# Problem: Transform Array by Parity
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        oc=0
        ec=0
        for i in nums :
            if i%2:
                oc+=1
            else:
                ec+=1
        idx=0
        while ec>0:
            nums[idx]=0
            idx+=1
            ec-=1
        while oc>0:
            nums[idx]=1
            idx+=1
            oc-=1
        return nums
