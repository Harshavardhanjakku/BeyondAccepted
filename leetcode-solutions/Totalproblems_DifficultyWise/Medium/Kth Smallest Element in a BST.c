# Kth Smallest Element in a BST
# Difficulty: Medium
# Language: c

int l=0;

int inorder(struct TreeNode* root,int k){
    if(root==NULL)return -1;
    int left=inorder(root->left,k);
    if(l==k)return left;
    l++;
    if(l==k)return root->val;
    return inorder(root->right,k);
}

int kthSmallest(struct TreeNode* root,int k){
    l=0;
    return inorder(root,k);
}
