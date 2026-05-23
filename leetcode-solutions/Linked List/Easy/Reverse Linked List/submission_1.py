# Problem: Reverse Linked List
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
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None :
            return head
        else:
            prev=head
            temp=prev.next
            curr=temp.next
            prev.next=None
            while curr is not None :
                temp.next=prev
                prev=temp
                temp=curr
                curr=curr.next
            temp.next=prev
            return temp

        
