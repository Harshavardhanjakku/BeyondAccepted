# Problem: Palindrome Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: python
# Submission: 2

class Solution(object):
    def isPalindrome(self, head):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        return l==l[::-1]
