# Problem: 3Sum
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 1):
            dic = {}
            for j in range(i + 1, n):
                target = - (nums[i] + nums[j])
                if target in dic:
                    triplet = [nums[i], nums[j], target]
                    if triplet not in res:
                        res.append(triplet)
                else:
                    dic[nums[j]] = True
        return res

