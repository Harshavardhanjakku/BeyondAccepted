# Problem: Detect Capital
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capitalflag=True
        smallflag=True
        titleflag=True
        count=1
        for i in word:
            flag=i.isupper()
            if not flag :
                capitalflag=False
            if flag:
                smallflag=False
            if count==1 and not flag :
                titleflag=False
            elif count>1 and flag:
                titleflag=False

            count+=1
        return capitalflag or smallflag or titleflag


