# Unique 3-Digit Even Numbers
# Difficulty: Easy
# Language: python

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        n=len(digits)
        res=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    num=(100*digits[i])+(10*digits[j])+digits[k]
                    if (digits[k]%2==0) and (i!=j) and (j!=k) and (k!=i) and (num not in res) and digits[i]!=0 :
                        res.add(num)
        
        return len(res)
