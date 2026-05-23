# Problem: Find Unique Binary String
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findDifferentBinaryString(self, nums):
        res=""
        for i in range(len(nums)):
            if nums[i][i]=="0":
                res+="1"
            else:
                res+="0"
        return res
