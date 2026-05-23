# Problem: Delete Node in a Linked List
# Difficulty: Medium
# Topic: Linked List
# Language: c
# Submission: 1

void deleteNode(struct ListNode* node) {
    if (node == NULL || node->next == NULL) return; // safety
    struct ListNode* temp = node->next;
    node->val = temp->val;
    node->next = temp->next;
    free(temp);
}

