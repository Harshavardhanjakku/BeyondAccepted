# Problem: Search in Rotated Sorted Array
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def search(self,nums,target):
        if target in nums :
            return nums.index(target)
        else:
            return -1
