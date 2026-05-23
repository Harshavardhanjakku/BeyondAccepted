# Problem: Check if Numbers Are Ascending in a Sentence
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.split()
        l=[int(x) for x in s if x.isdigit()]
        for i in range(len(l)-1):
            if l[i]>=l[i+1]:
                return False
        return True
