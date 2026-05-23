# Problem: Sort List
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        res=[]
        while temp :
            res.append(temp.val)
            temp=temp.next
        res.sort()
        i=0
        temp=head
        while temp:
            temp.val=res[i]
            i+=1
            temp=temp.next
        return head

        
