# Problem: Shuffle the Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n):
            nums[i]=nums[i]+nums[i+n]*1001
        j=2*n-1
        for i in range(n):
            idx=n-i-1
            x,y=nums[idx]%1001,nums[idx]//1001
            nums[j-1],nums[j]=x,y
            j-=2
        print(nums)
        return nums



