# Delete Node in a Linked List
# Difficulty: Medium
# Language: c

void deleteNode(struct ListNode* node) {
    if (node == NULL || node->next == NULL) return; // safety
    struct ListNode* temp = node->next;
    node->val = temp->val;
    node->next = temp->next;
    free(temp);
}

