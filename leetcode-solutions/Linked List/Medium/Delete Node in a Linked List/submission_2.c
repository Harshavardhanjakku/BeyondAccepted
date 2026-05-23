# Problem: Delete Node in a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: c
# Submission: 2

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void deleteNode(struct ListNode* node) {
    struct ListNode* temp = node->next;
    node->val = temp->val;
    node->next = temp->next;
    free(temp);  
}

