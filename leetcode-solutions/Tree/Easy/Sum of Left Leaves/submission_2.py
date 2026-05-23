# Problem: Sum of Left Leaves
# Difficulty: Easy
# Topic: Tree
# Language: python
# Submission: 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        s=[0]
        def dfs(root,flag):
            if root is None:
                return
            if flag and root.left is None and root.right is None:
                s[0]+=root.val
            dfs(root.left,True)
            dfs(root.right,False)
        dfs(root,False)
        return s[0]
