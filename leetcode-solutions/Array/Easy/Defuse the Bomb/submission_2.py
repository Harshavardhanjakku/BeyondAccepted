# Problem: Defuse the Bomb
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        if k==0:
            return [0]*(n)
        elif k>0:
            code.extend(code[:k])
            res=[]
            tot=sum(code[1:k+1])
            res.append(tot)
            for i in range(1,n):
                tot-=code[i]
                tot+=code[i+k]
                res.append(tot)
            return res
        else:
            code=code[k:]+code
            tot=sum(code[:abs(k)])
            res=[]
            res.append(tot)
            k=abs(k)
            for i in range(1+k,n+k):
                tot+=code[i-1]
                tot-=code[i-k-1]
                res.append(tot)
            return res


