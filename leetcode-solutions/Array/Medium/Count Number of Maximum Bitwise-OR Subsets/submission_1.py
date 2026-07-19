# Problem: Count Number of Maximum Bitwise-OR Subsets
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def countMaxOrSubsets(self, nums):
        maxi = 0
        for x in nums:
            maxi |= x
        n = len(nums)
        def dfs(i, curr):
            if i == n:
                return 1 if curr == maxi else 0
            take = dfs(i + 1, curr | nums[i])
            dontTake = dfs(i + 1, curr)
            return take + dontTake
        return dfs(0, 0)
