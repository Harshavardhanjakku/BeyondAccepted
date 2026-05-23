# Problem: Rotate List
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
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        n=0
        temp=head
        while temp is not None :
            n+=1
            temp=temp.next
        if n==0:
            return head
        k=k%n
        if k==0:
            return head
        i=1
        temp=head 
        while i<=k: 
            temp=temp.next
            i+=1
        
        curr=head
        while temp.next:
            curr=curr.next
            temp=temp.next

        print(curr.val)
        print(temp.val)
        prev=curr.next
        curr.next=None
        temp.next=head
        return prev
