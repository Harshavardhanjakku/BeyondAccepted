# Problem: Find N Unique Integers Sum up to Zero
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[] 
        for i in range(1,n): 
            res.append(i)
        mysum=(((n-1)*(n))//2)*-1
        res.append(mysum)
        return res
        
