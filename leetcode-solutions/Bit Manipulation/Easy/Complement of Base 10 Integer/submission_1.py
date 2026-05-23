# Problem: Complement of Base 10 Integer
# Difficulty: Easy
# Topic: Bit Manipulation
# Language: python
# Submission: 1

import math
class Solution(object):
    def bitwiseComplement(self,n):
        if n==0:return 1
        comp=~n
        bits=int(math.log(n,2))+1
        mask=(1<<bits)-1
        return comp&mask
