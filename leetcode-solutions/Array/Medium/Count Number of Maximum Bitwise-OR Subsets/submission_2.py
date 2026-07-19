# Problem: Count Number of Maximum Bitwise-OR Subsets
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def countMaxOrSubsets(self, nums):
        maxi = 0
        for x in nums:
            maxi |= x
        n = len(nums)
        total = 0
        for mask in range(1 << n):   
            curr = 0
            for j in range(n):
                if mask & (1 << j):      
                    curr |= nums[j]
            if curr == maxi:
                total += 1
        return total
