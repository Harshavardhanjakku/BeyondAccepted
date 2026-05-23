# Problem: Palindrome Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: python3
# Submission: 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        return l==l[::-1]
