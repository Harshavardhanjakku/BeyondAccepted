# Problem: Remove Duplicates from Sorted List II
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 1

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr: 
            if curr.next and curr.val == curr.next.val: 
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next

