# Problem: Check If It Is a Good Array
# Difficulty: Hard
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 1. 1 unte return true 
        # 2. sort chesi number divisible ayyi unte return False
        # 3.
        import math
        myhcf=math.gcd(*nums)
        if myhcf==1:
            return True
        
        return False
