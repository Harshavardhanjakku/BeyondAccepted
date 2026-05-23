# Problem: Shuffle the Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def shuffle(self, nums, n):
        BASE = 1001
        
        for i in range(n):
            nums[i] = nums[i] + nums[i+n] * BASE
        
        j = 2*n - 1
        for idx in range(n-1, -1, -1):
            x = nums[idx] % BASE
            y = nums[idx] // BASE
            nums[j-1], nums[j] = x, y
            j -= 2
        
        return nums

