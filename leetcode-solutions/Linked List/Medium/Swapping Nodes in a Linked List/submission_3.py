# Problem: Swapping Nodes in a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        temp=head
        fast=head
        i=1
        while i<=k:
            temp=fast
            fast=fast.next
            i+=1
        slow=head
        while fast:
            slow=slow.next
            fast=fast.next
        slow.val,temp.val=temp.val,slow.val
        return head
