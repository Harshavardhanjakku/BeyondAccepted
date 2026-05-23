# Count Prefixes of a Given String
# Difficulty: Easy
# Language: python3

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        c=0
        for i in words:
            if s.startswith(i):
                c+=1
        return c
