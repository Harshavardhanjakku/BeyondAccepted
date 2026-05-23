# Delete the Middle Node of a Linked List
# Difficulty: Medium
# Language: c

struct ListNode* deleteMiddle(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* prev = head;

    if (slow->next == NULL) {
        free(head);
        return NULL;
    }

    while (fast != NULL && fast->next != NULL) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    prev->next = slow->next;
    free(slow);
    return head;
}

