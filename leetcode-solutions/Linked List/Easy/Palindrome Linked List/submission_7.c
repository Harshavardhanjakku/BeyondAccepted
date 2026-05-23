# Problem: Palindrome Linked List
# Difficulty: Easy
# Topic: Linked List
# Language: c
# Submission: 7

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdbool.h>
#include <stdlib.h>

struct ListNode* reverse(struct ListNode* head, int len, struct ListNode** next_half) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next = NULL;
    for (int i = 0; i < len; ++i) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *next_half = curr; // Remaining list after reversal
    return prev; // Head of reversed part
}

bool isPalindrome(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return true;
    }

    int length = 0;
    struct ListNode* temp = head;
    while (temp) {
        length++;
        temp = temp->next;
    }

    struct ListNode* second_half = NULL;
    struct ListNode* first_half_reversed = reverse(head, length / 2, &second_half);

    if (length % 2 == 1) {
        second_half = second_half->next;
    }

    struct ListNode* p1 = first_half_reversed;
    struct ListNode* p2 = second_half;
    while (p1 && p2) {
        if (p1->val != p2->val) {
            return false;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    return true;
}

