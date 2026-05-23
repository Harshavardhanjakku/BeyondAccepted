# Problem: Count Complete Tree Nodes
# Difficulty: Easy
# Topic: Binary Search
# Language: python
# Submission: 4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def mytraversal(root):
            if not root:
                return 0
            lc=mytraversal(root.left)
            rc=mytraversal(root.right)
            return 1+lc+rc
        return mytraversal(root)

