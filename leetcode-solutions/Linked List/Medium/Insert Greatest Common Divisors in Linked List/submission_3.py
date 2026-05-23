# Problem: Insert Greatest Common Divisors in Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def gcd(a,b):
        r=b%a
        if r==0:
            return a
        else:
            return gcd(r,a)
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        else:
            temp=head
            while temp.next is not None:
                prev=temp
                curr=temp.next
                newnode=ListNode(gcd(prev.val,curr.val),None)
                prev.next=newnode
                newnode.next=curr
                temp=curr
            return head

            
