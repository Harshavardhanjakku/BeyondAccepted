# Find the K-th Character in String Game I
# Difficulty: Easy
# Language: python3

class Solution:
    def kthCharacter(self, k: int) -> str:
        def generatestring(k,s,mylen):
            if mylen//2>k:
                return s
            ns=s
            for i in s:
                ns+=chr(ord(i)+1)
            return generatestring(k-1,ns,mylen*2) 
        return generatestring(k,"a",1)[k-1]
        
