# Detect Capital
# Difficulty: Easy
# Language: python

class Solution(object):
    def detectCapitalUse(self, word):
        capitalflag=True
        smallflag=True
        titleflag=True
        first=True
        for ch in word:
            if ch.isupper():
                smallflag=False
            else:
                capitalflag=False
            if first:
                if not ch.isupper():
                    titleflag=False
                first=False
            else:
                if ch.isupper():
                    titleflag=False
        return capitalflag or smallflag or titleflag
