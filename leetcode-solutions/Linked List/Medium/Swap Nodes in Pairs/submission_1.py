# Problem: Swap Nodes in Pairs
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        while temp and temp.next:
            temp.val,temp.next.val=temp.next.val,temp.val
            temp=temp.next.next
        return head

