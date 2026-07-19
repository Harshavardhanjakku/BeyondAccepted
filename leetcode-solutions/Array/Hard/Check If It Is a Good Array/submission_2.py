# Problem: Check If It Is a Good Array
# Difficulty: Hard
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 1. 1 unte return true 
        # 2. sort chesi number divisible ayyi unte return False
        # 3.
        import math
        if 1 in nums :
            return True 
        n=len(nums)
        if n<=1:
            return False 
        # nums.sort()
        # a=min(nums)
        # b=None
        # for num in nums :
        #     if a!=num:
        #         b=num
        #         break
        myhcf=math.gcd(*nums)
        if myhcf==1:
            return True
        
        return False
