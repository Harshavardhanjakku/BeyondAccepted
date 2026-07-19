# Problem: Partition Array According to Given Pivot
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left=[]
        mid=[]
        right=[]

        for i in nums:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                right.append(i)
        nums[:] = left + mid + right
        return nums
