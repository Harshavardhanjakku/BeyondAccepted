# Problem: Sort List
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 1

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None

        left=self.sortList(head)
        right=self.sortList(mid)

        return self.merge(left,right)

    def merge(self,l1,l2):
        dummy=ListNode(0)
        temp=dummy

        while l1 and l2:
            if l1.val<l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next

            temp=temp.next

        if l1:
            temp.next=l1

        if l2:
            temp.next=l2

        return dummy.next
