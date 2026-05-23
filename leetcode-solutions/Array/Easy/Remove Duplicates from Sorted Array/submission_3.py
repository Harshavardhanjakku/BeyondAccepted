# Problem: Remove Duplicates from Sorted Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        i = j = 0
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return i + 1
