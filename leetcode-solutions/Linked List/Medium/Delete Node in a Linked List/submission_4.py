# Problem: Delete Node in a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: python
# Submission: 4

class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next
