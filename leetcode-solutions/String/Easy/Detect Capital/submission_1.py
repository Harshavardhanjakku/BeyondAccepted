# Problem: Detect Capital
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

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
