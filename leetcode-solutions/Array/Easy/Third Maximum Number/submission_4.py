# Problem: Third Maximum Number
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 4

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        res=[]
        count=0
        for i in nums :
            if i not in s :
                s.add(i)
                res.append(i)
                count+=1
        res.sort()
        return res[-1] if count<3 else res[-3]


        
