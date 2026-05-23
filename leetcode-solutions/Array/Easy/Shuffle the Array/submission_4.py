# Problem: Shuffle the Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        n=len(nums)
        nw=[]
        for i in range(n//2):
                nw.append(nums[i])
                nw.append(nums[n//2+i])
        return nw
        
