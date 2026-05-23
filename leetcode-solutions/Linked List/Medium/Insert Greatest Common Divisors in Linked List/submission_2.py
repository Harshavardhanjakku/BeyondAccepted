# Problem: Insert Greatest Common Divisors in Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python3
# Submission: 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        import math
        def insertmiddle(left,right):
            a=left.val
            b=right.val
            result = math.gcd(a, b)
            newnode=ListNode(result)
            left.next=newnode
            newnode.next=right
        if not head or not head.next:
            return head
        curr=head
        while curr and curr.next is not None :
            nptr=curr.next
            insertmiddle(curr,nptr)
            curr=nptr
        return head
