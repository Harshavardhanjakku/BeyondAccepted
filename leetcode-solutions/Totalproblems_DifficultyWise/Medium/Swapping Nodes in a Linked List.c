# Swapping Nodes in a Linked List
# Difficulty: Medium
# Language: c

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct ListNode* temp = head;
    for (int i = 1; i < k; i++) {
        temp = temp->next;
    }
    struct ListNode* first = temp;

    struct ListNode* fast = first->next;
    struct ListNode* slow = head;
    while (fast != NULL) {
        slow = slow->next;
        fast = fast->next;
    }

    int t = first->val;
    first->val = slow->val;
    slow->val = t;

    return head;
}

