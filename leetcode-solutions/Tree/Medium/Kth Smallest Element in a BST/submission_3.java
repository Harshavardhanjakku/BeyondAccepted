# Problem: Kth Smallest Element in a BST
# Difficulty: Medium
# Topic: Tree
# Language: java
# Submission: 3

class Solution{
    int l=0;
    public int kthSmallest(TreeNode root,int k){
        return inorder(root,k);
    }
    public Integer inorder(TreeNode root,int k){
        if(root==null)return null;
        Integer left=inorder(root.left,k);
        if(left!=null)return left;
        l++;
        if(l==k)return root.val;
        return inorder(root.right,k);
    }
}
