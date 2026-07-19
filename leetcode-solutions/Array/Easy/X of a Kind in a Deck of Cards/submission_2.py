# Problem: X of a Kind in a Deck of Cards
# Difficulty: Easy
# Topic: Array
# Language: python3
# Submission: 2

from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = {}
        for card in deck:
            freq[card] = freq.get(card, 0) + 1
        g = 0
        for count in freq.values():
            g = gcd(g, count)
        return g >= 2
