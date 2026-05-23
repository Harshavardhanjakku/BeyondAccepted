# Convert Binary Number in a Linked List to Integer
# Difficulty: Easy
# Language: python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        temp=head
        res=0
        while temp :
            res+=temp.val*(2**(count-1))
            count-=1
            temp=temp.next
        return res
