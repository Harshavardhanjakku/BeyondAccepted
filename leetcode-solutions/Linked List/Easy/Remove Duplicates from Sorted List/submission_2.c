# Problem: Remove Duplicates from Sorted List
# Difficulty: Easy
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
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *temp=head;
    while(temp!=NULL && temp->next!=NULL)
    {
        if (temp->next!=NULL && temp->val==temp->next->val)
        {
            temp->next=temp->next->next;
        }
        else
        temp=temp->next;
    }
    return head;
}
