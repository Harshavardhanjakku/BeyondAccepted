# Problem: X of a Kind in a Deck of Cards
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 1

from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        count=Counter(deck).values()
        return reduce(gcd,count) > 1
