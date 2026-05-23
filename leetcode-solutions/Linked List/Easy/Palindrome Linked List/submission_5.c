# Problem: Palindrome Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: c
# Submission: 5

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdbool.h>

struct ListNode* rev(struct ListNode* head, int l, struct ListNode** cur) {
    struct ListNode* r = NULL;
    *cur = head;
    for (int i = 0; i < l; ++i) {
        struct ListNode* nxt = (*cur)->next;
        (*cur)->next = r;
        r = *cur;
        *cur = nxt;
    }
    return r;
}

bool isPalindrome(struct ListNode* head) {
    int l = 0;
    struct ListNode* temp = head;
    while (temp) {
        l += 1;
        temp = temp->next;
    }
    
    if (l == 1) {
        return true;
    }

    struct ListNode* h;
    struct ListNode* r = rev(head, l / 2, &h);

    if (l % 2 == 1) {
        h = h->next;
    }

    for (int i = 0; i < l / 2; ++i) {
        if (r->val != h->val) {
            return false;
        }
        r = r->next;
        h = h->next;
    }

    return true;
}

