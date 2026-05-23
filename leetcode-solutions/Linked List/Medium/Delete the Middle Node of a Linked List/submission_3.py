# Problem: Delete the Middle Node of a Linked List
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
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        prev=head 
        if slow.next is None :
            head=None 
            return head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head 
        
        
