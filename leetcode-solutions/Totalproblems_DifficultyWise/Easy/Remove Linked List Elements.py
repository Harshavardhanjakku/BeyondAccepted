# Remove Linked List Elements
# Difficulty: Easy
# Language: python

class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return head
        while head is not None and head.val == val:
            head = head.next
        temp = head
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next 
            else:
                temp = temp.next  
        return head

