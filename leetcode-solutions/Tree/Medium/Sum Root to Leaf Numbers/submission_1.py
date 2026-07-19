# Problem: Sum Root to Leaf Numbers
# Difficulty: Medium
# Topic: Tree
# Language: python3
# Submission: 1

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr):
            if not root:
                return 0
            curr = curr * 10 + root.val
            if not root.left and not root.right:
                return curr
            return dfs(root.left, curr) + dfs(root.right, curr)
        return dfs(root, 0)
