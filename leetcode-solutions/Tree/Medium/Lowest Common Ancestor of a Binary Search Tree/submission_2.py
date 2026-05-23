# Problem: Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 2

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

