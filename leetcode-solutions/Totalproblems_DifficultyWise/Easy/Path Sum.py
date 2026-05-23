# Path Sum
# Difficulty: Easy
# Language: python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        leftcall=self.hasPathSum(root.left,targetSum - root.val)
        rightcall=self.hasPathSum(root.right, targetSum - root.val)
        return leftcall or rightcall
