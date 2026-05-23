# Problem: Linked List Cycle
# Difficulty: Easy
# Topic: Hash Table
# Language: c
# Submission: 1

typedef struct ListNode node;
bool hasCycle(struct ListNode *head) {
    node *slow = head;
    node *fast = head;
    while (fast!=NULL && fast->next!=NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow==fast)
        {
            return true;
            break;
        }
    }
   return false;
}
