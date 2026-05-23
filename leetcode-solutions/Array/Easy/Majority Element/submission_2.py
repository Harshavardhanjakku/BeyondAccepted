# Problem: Majority Element
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        count=0
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
            count+=1
        for i in dic:
            if dic[i]>count//2:
                return i
                break
