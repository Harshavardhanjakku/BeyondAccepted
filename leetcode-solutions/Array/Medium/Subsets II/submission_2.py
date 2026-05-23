# Problem: Subsets II
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        s = set()
        nums.sort()          
        n = len(nums)

        for i in range(1 << n):
            temp = []
            for j in range(n):
                if (i >> j) & 1:
                    temp.append(nums[j])

            key = tuple(temp)  
            if key not in s:
                res.append(temp)
                s.add(key)

        return res

