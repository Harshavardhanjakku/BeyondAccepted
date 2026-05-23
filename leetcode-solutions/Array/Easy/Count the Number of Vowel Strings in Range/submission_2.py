# Problem: Count the Number of Vowel Strings in Range
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        s={'a', 'e', 'i', 'o', 'u'}
        c=0
        for i in range(left,right+1):
            temp=words[i]
            l=len(temp)
            if (temp[0] in s) and (temp[l-1] in s):
                c+=1
        return c

