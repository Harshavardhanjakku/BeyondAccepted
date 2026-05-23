# Defuse the Bomb
# Difficulty: Easy
# Language: python

class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        
        if k == 0:
            return [0] * n
         
        if k > 0:
            code = code + code[:k]
            res = []
            tot = sum(code[1:k+1])
            res.append(tot)
            
            for i in range(1, n):
                tot -= code[i]
                tot += code[i+k]
                res.append(tot)
            
            return res
         
        k = -k
        code = code[-k:] + code
        res = []
        tot = sum(code[:k])
        res.append(tot)
        
        for i in range(1, n):
            tot += code[i+k-1]
            tot -= code[i-1]
            res.append(tot)
        
        return res

