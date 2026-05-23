# Problem: Middle of the Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: python
# Submission: 1

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
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next  
        c=0
        while c<n//2 and head:
            head=head.next
            c+=1
        return head
