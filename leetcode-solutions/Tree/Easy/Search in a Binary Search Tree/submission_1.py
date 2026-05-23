# Problem: Search in a Binary Search Tree
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
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while root:
            if val<root.val:
                root=root.left
            elif val>root.val:
                root=root.right
            else:
                return root
        return root
