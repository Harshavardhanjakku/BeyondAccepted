# Problem: Linked List Cycle II
# Difficulty: Medium
# Topic: Hash Table
# Language: python
# Submission: 1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        else:
            return None
        temp=head
        while temp!=slow:
            slow=slow.next
            temp=temp.next
        return temp
