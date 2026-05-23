# Problem: Kth Smallest Element in a BST
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 4

class Solution(object):
    def kthSmallest(self, root, k):
        self.l = 0
        def inorder(root):
            if not root:
                return None
            left = inorder(root.left)
            if left is not None:
                return left
            self.l += 1
            if self.l == k:
                return root.val
            return inorder(root.right)
        return inorder(root)
