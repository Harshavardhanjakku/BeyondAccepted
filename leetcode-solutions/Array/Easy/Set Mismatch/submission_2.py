# Problem: Set Mismatch
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        sofn=(n*(n+1))//2
        tot=sum(nums)
        difference=sofn-tot
        sqtot=0
        for i in nums :
            sqtot+=i*i
        sofsq=(n*(n+1)*(2*n+1))//6
        squaresdiff=sofsq-sqtot
        addition=squaresdiff//difference
        return [(addition-difference)//2,(addition+difference)//2]
