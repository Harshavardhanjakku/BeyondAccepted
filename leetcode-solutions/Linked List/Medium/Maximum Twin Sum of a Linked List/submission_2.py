# Problem: Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python3
# Submission: 2

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

        ans = 0

        while slow:
            ans = max(ans, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return ans
