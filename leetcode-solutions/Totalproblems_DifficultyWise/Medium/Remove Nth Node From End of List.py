# Remove Nth Node From End of List
# Difficulty: Medium
# Language: python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            head=None
            return head
        fast=head
        i=1
        while i<=n:
            i+=1
            fast=fast.next
        slow=head
        if fast is None :
            return head.next
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        prev.next=slow.next
        return head

