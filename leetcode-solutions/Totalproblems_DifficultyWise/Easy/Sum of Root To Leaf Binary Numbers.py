# Sum of Root To Leaf Binary Numbers
# Difficulty: Easy
# Language: python

class Solution(object):
    def sumRootToLeaf(self, root):
        self.res = 0
        def dfs(node, num):
            if not node:
                return
            num = num * 2 + node.val
            if not node.left and not node.right:
                self.res += num
                return
            dfs(node.left, num)
            dfs(node.right, num)
        dfs(root, 0)
        return self.res
