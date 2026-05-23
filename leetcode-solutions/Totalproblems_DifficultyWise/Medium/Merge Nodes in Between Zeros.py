# Merge Nodes in Between Zeros
# Difficulty: Medium
# Language: python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        np=None
        prev=None
        temp=head.next
        tot=0
        zflag=False
        while temp is not None: 
            if temp.val==0:
                zflag=True
            if zflag:
                if np is None:
                    newnode=ListNode(tot)
                    np=newnode
                    prev=np
                else:
                    newnode=ListNode(tot)
                    prev.next=newnode
                    prev=newnode
                tot=0
                zflag=False
            tot+=temp.val
            temp=temp.next
        return np
