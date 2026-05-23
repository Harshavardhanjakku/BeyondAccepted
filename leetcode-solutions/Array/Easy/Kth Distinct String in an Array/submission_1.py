# Problem: Kth Distinct String in an Array
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        l=[]
        for i in arr:
            if arr.count(i)==1:
                l.append(i)
        return l[k-1] if k<=len(l) else ""
            
