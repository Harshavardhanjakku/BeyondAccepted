# Problem: Swapping Nodes in a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 2

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        temp = head
        for i in range(k - 1):
            temp = temp.next
        first = temp

        fast = first.next
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next

        first.val, slow.val = slow.val, first.val

        return head

