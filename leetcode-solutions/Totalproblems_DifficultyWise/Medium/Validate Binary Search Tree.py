# Validate Binary Search Tree
# Difficulty: Medium
# Language: python

class Solution(object):
    def isValidBST(self, root):
        self.prev = None
        def traversal(node):
            if not node:
                return True
            if not traversal(node.left):
                return False  
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            return traversal(node.right)
        return traversal(root)
