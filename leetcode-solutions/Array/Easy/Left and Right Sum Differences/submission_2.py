# Problem: Left and Right Sum Differences
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lc=0
        rc=0
        l=[]
        r=[]
        n=len(nums)
        for i in range(n):
            l.append(lc)
            lc+=nums[i]
            r.insert(0,rc)
            rc+=nums[n-i-1]
        s=[]
        for i in range(n):
            s.append(abs(l[i]-r[i]))
        return s
        
