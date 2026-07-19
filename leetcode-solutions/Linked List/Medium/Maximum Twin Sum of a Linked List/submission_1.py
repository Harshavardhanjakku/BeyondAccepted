# Problem: Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python3
# Submission: 1

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        maxi = 0

        while slow:
            s = prev.val + slow.val
            if s > maxi:
                maxi = s

            prev = prev.next
            slow = slow.next

        return maxi
