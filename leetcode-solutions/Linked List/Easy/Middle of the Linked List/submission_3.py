# Problem: Middle of the Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: python
# Submission: 3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        fast=head
        while fast is not None and fast.next is not None:
            temp=temp.next
            fast=fast.next.next
        return temp
