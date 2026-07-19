# Problem: Sum Root to Leaf Numbers
# Difficulty: Medium
# Topic: Tree
# Language: python3
# Submission: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total=0
        def dfs(root,curr):
            nonlocal total
            if not root:
                return  
            curr=curr*10+root.val
            if not root.left and not root.right:
                total+=curr
            dfs(root.left,curr)
            dfs(root.right,curr)
        dfs(root,0)
        return total
