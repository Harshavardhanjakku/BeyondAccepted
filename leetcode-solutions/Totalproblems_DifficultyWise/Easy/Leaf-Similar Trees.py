# Leaf-Similar Trees
# Difficulty: Easy
# Language: python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        leafnodelist1=self.leafnodes(root1,[])
        leafnodelist2=self.leafnodes(root2,[])
        if leafnodelist1==leafnodelist2:
            return True
        else:
            return False
    def leafnodes(self,root,mylist):
        if root is None :
            return []
        elif root.left is None and root.right is None:
            return mylist+[root.val]
        else:
            return self.leafnodes(root.left,mylist)+self.leafnodes(root.right,mylist)

    
