# Problem: Maximum Prime Difference
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def checkprime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        n=len(nums)
        i,j=0,n-1
        while not checkprime(nums[i]):
            i+=1
        while not checkprime(nums[j]):
            j-=1
        return j-i
