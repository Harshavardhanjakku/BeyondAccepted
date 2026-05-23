# Problem: Prime In Diagonal
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
   
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def checkprime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        n=len(nums)
        maxi=0
        for i in range(n):
                val=nums[i][i]
                if checkprime(val):
                    maxi=max(maxi,val)
                val=nums[i][n-i-1] 
                if checkprime(val):
                    maxi=max(maxi,val)
        return maxi
        
