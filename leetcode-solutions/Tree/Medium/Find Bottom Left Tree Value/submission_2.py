# Problem: Find Bottom Left Tree Value
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 2

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = -1
        self.leftmost = None

        def dfs(node, depth):
            if not node:
                return 
            if depth > self.max_depth:
                self.max_depth = depth
                self.leftmost = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.leftmost

