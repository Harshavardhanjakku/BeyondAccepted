# Problem: 4Sum
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def fourSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = []
            dic[num].append(i)
        n = len(nums)
        s = set()
        res = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    tot = nums[i] + nums[j] + nums[k]
                    need = target - tot
                    if need in dic:
                        for idx in dic[need]:
                            if idx != i and idx != j and idx != k:
                                t = tuple(sorted([nums[i], nums[j], nums[k], need]))
                                if t not in s:
                                    s.add(t)
                                    res.append(list(t))
                                break
        return res
