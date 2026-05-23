# Problem: Intersection of Two Linked Lists
# Difficulty: Easy
# Topic: Hash Table
# Language: python
# Submission: 1

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
