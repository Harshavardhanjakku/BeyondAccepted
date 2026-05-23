# Valid Palindrome
# Difficulty: Easy
# Language: python

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
