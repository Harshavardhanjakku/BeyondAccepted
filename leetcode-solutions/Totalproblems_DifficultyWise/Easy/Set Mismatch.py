# Set Mismatch
# Difficulty: Easy
# Language: python

class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)

        sofn = n * (n + 1) // 2
        sofsq = n * (n + 1) * (2*n + 1) // 6

        tot = sum(nums)
        sqtot = sum(x*x for x in nums)

        difference = sofn - tot           
        squaresdiff = sofsq - sqtot          

        addition = squaresdiff // difference 

        D = (addition - difference) // 2
        M = (addition + difference) // 2

        return [D, M]

