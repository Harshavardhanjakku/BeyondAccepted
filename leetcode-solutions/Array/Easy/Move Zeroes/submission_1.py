# Problem: Move Zeroes
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        
        return nums
