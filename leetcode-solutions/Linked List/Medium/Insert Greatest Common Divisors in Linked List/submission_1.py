# Problem: Insert Greatest Common Divisors in Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python3
# Submission: 1

class Solution:
    def insertGreatestCommonDivisors(self, head):
        import math

        def insertmiddle(left, right):
            a = left.val
            b = right.val
            result = math.gcd(a, b)
            newnode = ListNode(result)
            left.next = newnode
            newnode.next = right

        if not head or not head.next:
            return head

        curr = head
        while curr and curr.next is not None:
            nptr = curr.next
            insertmiddle(curr, nptr)
            curr = nptr

        return head
