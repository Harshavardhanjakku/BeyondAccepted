# Problem: Valid Palindrome
# Difficulty: Easy
# Topic: Two Pointers
# Language: python
# Submission: 1

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        myStr=''
        for i in s:
            if i.isalnum():
                myStr+=i
        myStr=lower(myStr)
        if myStr==myStr[::-1]:
            return True
        else:
            return False
