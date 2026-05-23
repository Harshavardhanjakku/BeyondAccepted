# Balanced Binary Tree
# Difficulty: Easy
# Language: python

class Solution(object):
    def isBalanced(self, root):
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
        return height(root) != -1
