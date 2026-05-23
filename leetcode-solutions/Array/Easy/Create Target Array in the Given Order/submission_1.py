# Problem: Create Target Array in the Given Order
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target=[]
        ind=0
        for i in index:
            target.insert(i,nums[ind])
            ind+=1
        return target
