# Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Language: c

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    while (root != NULL) {
        if (root->val > p->val && root->val > q->val) {
            root = root->left;
        } else if (root->val < p->val && root->val < q->val) {
            root = root->right;
        } else {
            return root;
        }
    }
    return NULL;
}

