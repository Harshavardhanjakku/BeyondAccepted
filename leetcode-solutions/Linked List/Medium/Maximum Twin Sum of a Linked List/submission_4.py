# Problem: Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python3
# Submission: 4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev = None   
        curr = slow  
        while curr:
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward
        p1=head
        p2=prev
        maxi=0
        while p1 and p2:
            maxi=max(maxi,p1.val+p2.val)
            p1=p1.next
            p2=p2.next
        return maxi

