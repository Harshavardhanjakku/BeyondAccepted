# Problem: Minimum Common Value
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dic={}
        for i in nums1:
            dic[i]=dic.get(i,0)+1
        mini=float('inf')
        for i in nums2:
            if i in dic:
                mini=min(i,mini)
        return mini  if mini!=float('inf') else -1

