# Problem: Palindrome Number
# Difficulty: Easy
# Topic: Math
# Language: python3
# Submission: 6

class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=str(x)
        if r==r[::-1]:
            return True
        else:
            return False
        
