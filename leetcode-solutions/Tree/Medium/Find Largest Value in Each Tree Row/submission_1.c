# Problem: Find Largest Value in Each Tree Row
# Difficulty: Medium
# Topic: Tree
# Language: c
# Submission: 1

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* largestValues(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;

    if (!root) {
        return NULL;
    }

    struct TreeNode* queue[10000];
    int front = 0, rear = 0;

    queue[rear++] = root;

    int* res = (int*)malloc(sizeof(int) * 10000);

    while (front < rear) {
        int size = rear - front;
        int maxi = -2147483648;   // INT_MIN

        for (int i = 0; i < size; i++) {
            struct TreeNode* node = queue[front++];

            if (node->val > maxi)
                maxi = node->val;

            if (node->left)
                queue[rear++] = node->left;

            if (node->right)
                queue[rear++] = node->right;
        }

        res[(*returnSize)++] = maxi;
    }

    return res;
}
