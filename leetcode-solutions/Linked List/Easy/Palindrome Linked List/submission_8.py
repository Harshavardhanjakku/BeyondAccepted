# Problem: Palindrome Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: python
# Submission: 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def rev(head,l):
            r=None
            cur=head
            i=0
            for i in range(0,l):
                nxt=cur.next
                cur.next=r
                r=cur
                cur=nxt
            return r,cur
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        if l==1:
            return True
        r,h=rev(head,l//2)
        if l%2==1:
            h=h.next
        for i in range(0,l//2):
            if r.val!=h.val:
                return False
            r=r.next
            h=h.next
        return True
