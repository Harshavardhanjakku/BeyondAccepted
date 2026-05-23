# Problem: Shuffle the Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ind=0
        ans=[0]*(2*n)
        n=2*n
        for i in range(n//2):
            ans[ind]=nums[i]
            ans[ind+1]=nums[i+n//2]
            ind+=2
        return ans

