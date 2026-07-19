# Problem: Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python3
# Submission: 5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        temp=head
        while temp :
            l.append(temp.val)
            temp=temp.next
        maxi=0
        n=len(l)
        i=0
        j=n-1
        while i<j:
            maxi=max(maxi,l[i]+l[j])
            i+=1
            j-=1
        return maxi
        
