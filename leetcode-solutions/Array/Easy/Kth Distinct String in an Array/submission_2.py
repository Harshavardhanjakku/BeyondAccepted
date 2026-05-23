# Problem: Kth Distinct String in an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        myl=[]
        for i in arr:
            if arr.count(i)==1:
                myl.append(i)
        return myl[k-1] if k<=len(myl) else ""


        
