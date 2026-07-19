# Problem: Range Sum of BST
# Difficulty: Easy
# Topic: Tree
# Language: python
# Submission: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        s=[0]
        def dfs(root):
            
            if not root:
                return 
            if low<=root.val<=high:
                s[0]+=root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return s[0]
